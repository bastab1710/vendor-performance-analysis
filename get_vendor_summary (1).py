import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db  

# Logging setup
logging.basicConfig(
    filename="logs/get_vendor.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    '''Merge different tables to create vendor summary'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
        ),
        
        PurchaseSummary AS (
            SELECT
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price AS ActualPrice,
                pp.Volume,
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Rupees) AS TotalPurchaseRupees
            FROM purchases p
            JOIN purchase_prices pp
                ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
        ),
        
        SalesSummary AS (
            SELECT
                VendorNumber,
                Brand,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(SalesRupees) AS TotalSalesRupees,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            GROUP BY VendorNumber, Brand
        )
        
        SELECT
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseRupees,
            ss.TotalSalesQuantity,
            ss.TotalSalesRupees,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss
            ON ps.VendorNumber = ss.VendorNumber
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseRupees DESC""", conn)

    return vendor_sales_summary

def clean_data(df):
    '''Clean and enrich vendor summary data'''
    df['GrossProfit'] = df['TotalSalesRupees'] - df['TotalPurchaseRupees']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesRupees']) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesRupees'] / df['TotalPurchaseRupees']
    return df

if __name__ == '__main__':
    conn = sqlite3.connect('inventory.db')

    logging.info('Creating Vendor Summary Table.......')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data......')
    ingest_db(clean_df, 'vendor_sales_summary', conn)
    logging.info('Completed')
