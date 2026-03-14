# Vendor Performance Analysis

An end-to-end data analysis solution to help organizations measure and optimize vendor performance. By integrating supply chain data with statistical modeling, we identified key drivers of profitability and inventory efficiency.

---

## Project Structure

```
├── data/                   # Raw datasets created in MySQL Workbench
├── IngestionFiles/         # Data ingestion and DB automation scripts
│   ├── Ingestion.ipynb     # DB loading tests
│   └── ingestion_db.py     # Production ingestion script
├── EDAFiles/               # SQL transformations and logic
│   ├── Exploratory Data Analysis.ipynb
│   └── get_vendor_summary.py    # CTE-based data merging
├── VPA/                    # Statistical analysis & hypothesis testing
│   └── Vendor Performance Analysis.ipynb
├── FinalDataframe/         # Production-ready CSV
│   └── my_dataframe.csv   # The "Single Source of Truth"
├── ProjectDashboard/       # Interactive web frontend visualization
│   ├── index.html          # Secure login page
│   ├── dashboard.html      # Main metrics view
│   ├── style.css           # Custom UI styling
│   ├── script.js           # Modal logic and auth
│   └── images/             # Visual plot assets (PNGs)
├── logs/                   # System execution logs
└── inventory.db            # Final SQLite database
```

---

## Step 1: Data Creation & Ingestion

The project began by designing a relational database schema representing a retail supply chain.

- **Database Design:** Created 6 core tables (Begin Inventory, End Inventory, Purchase Prices, Purchases, Sales, Vendor Invoice) using MySQL Workbench.
- **Automated Pipeline:** Developed a Python script (`ingestion_db.py`) to automate the migration of raw CSVs into a local SQLite database (`inventory.db`), including automated logging for performance monitoring.

---

## Step 2: Business Logic & Data Transformation

In the `EDAFiles/` phase, we moved beyond raw data to create high-level business entities.

- **SQL CTEs:** Used Common Table Expressions in Python to join disparate tables, calculating Lead Times, Freight Costs, and Sales-to-Purchase ratios at the vendor level.
- **Feature Engineering:** Calculated critical KPIs like Gross Profit, Profit Margin, and Stock Turnover to identify vendor health.

---

## Step 3: Statistical Analysis & Hypothesis Testing

The `VPA/` phase involved deep-dive research to find actionable patterns.

- **T-Tests & Confidence Intervals:** Compared profit margins between top and low-performing vendors. Top vendors operate at a statistically significant higher margin (~97%), which is not due to random chance.
- **Correlation Analysis:** Used heatmaps to identify the link (0.96) between sales volume and logistics overhead.
- **Outlier Detection:** Used boxplots to identify "Slow-Moving" products with a Stock Turnover < 1.

---

## Step 4: Interactive Web Dashboard

The final output is a responsive Business Intelligence Dashboard that allows stakeholders to explore the findings.

- **Frontend Tech:** Built with HTML5, CSS3, and Vanilla JavaScript.
- **Secure Access:** Features a login gateway to protect sensitive vendor data.
- **Visual Insights:** A card-based layout where users can interact with modals to see detailed statistical plots and actionable business intelligence.

---

## Getting Started

### Prerequisites

- Python 3.x
- Libraries: `pandas`, `sqlalchemy`, `matplotlib`, `seaborn`, `scipy`

### Running the Analysis

```bash
# Ingest data
python IngestionFiles/ingestion_db.py

# Generate vendor summaries
python EDAFiles/get_vendor_summary.py
```

### Launching the Dashboard

1. Open the `/ProjectDashboard` folder
2. Launch `index.html` using Live Server in VS Code
3. Login with the credentials below:

| Field    | Value      |
|----------|------------|
| Username | `admin`    |
| Password | `password` |

---

## Contributors

- Uddipan Roy
- Nikita Das
- Bastabika Das