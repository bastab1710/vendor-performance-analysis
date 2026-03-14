document.addEventListener('DOMContentLoaded', () => {

    // --- LOGIN PAGE LOGIC ---
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const errorMessage = document.getElementById('login-error');

            // Simple validation for demo purposes
            if (username === 'admin' && password === 'password') {
                // Redirect to the dashboard
                window.location.href = 'dashboard.html';
            } else {
                errorMessage.textContent = 'Invalid username or password.';
            }
        });
    }

    // --- LOGOUT BUTTON LOGIC ---
    const logoutButton = document.getElementById('logout-button');
    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            // Redirect to the login page
            window.location.href = 'index.html';
        });
    }

    // --- DASHBOARD MODAL LOGIC (UPDATED FOR ANIMATIONS) ---
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const modalId = card.getAttribute('data-modal-target');
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.add('active'); // Add .active class to show
            }
        });
    });

    const closeButtons = document.querySelectorAll('.close-button');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal');
            modal.classList.remove('active'); // Remove .active class to hide
        });
    });

    // Close modal if user clicks outside the modal content
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            e.target.classList.remove('active'); // Remove .active class to hide
        }
    });

    // Close modal with the 'Escape' key
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal.active').forEach(modal => {
                modal.classList.remove('active');
            });
        }
    });
});