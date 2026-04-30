/* ============================================
   BOLD STORE - Main Application JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    initSearch();
    initFilters();
    initCartButtons();
    initScrollAnimations();
});

/* ============================================
   SEARCH FUNCTIONALITY
   ============================================ */

function initSearch() {
    const searchInput = document.getElementById('search');
    if (!searchInput) return;

    searchInput.addEventListener('input', function() {
        const value = this.value.toLowerCase();
        const cards = document.querySelectorAll('.card');

        cards.forEach(card => {
            const title = card.querySelector('.card-title');
            if (!title) return;

            const name = title.textContent.toLowerCase();
            const isVisible = name.includes(value);

            card.style.display = isVisible ? 'block' : 'none';
            if (isVisible) {
                card.classList.add('animate-fade');
            }
        });

        // Show empty state if no results
        const visibleCards = document.querySelectorAll('.card[style*="block"]');
        const emptyState = document.querySelector('.empty-state');
        if (emptyState) {
            emptyState.style.display = visibleCards.length === 0 ? 'block' : 'none';
        }
    });
}

/* ============================================
   CATEGORY FILTER
   ============================================ */

function initFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const category = this.dataset.category;
            
            // Update active state
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Filter products
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                if (category === 'all') {
                    card.style.display = 'block';
                } else {
                    const cardCategory = card.dataset.category;
                    card.style.display = cardCategory === category ? 'block' : 'none';
                }
                card.classList.add('animate-fade');
            });
        });
    });
}

/* ============================================
   ADD TO CART
   ============================================ */

function initCartButtons() {
    const addBtns = document.querySelectorAll('.btn-add-cart');
    
    addBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            
            // Add haptic feedback and visual effect
            this.style.transform = 'scale(0.95)';
            
            setTimeout(() => {
                this.style.transform = 'scale(1)';
                // Show toast notification
                showToast('Added to cart!', 'success');
            }, 150);

            // Submit the add to cart request
            const form = document.createElement('form');
            form.method = 'GET';
            form.action = `/add/${productId}/`;
            document.body.appendChild(form);
            form.submit();
        });
    });
}

/* ============================================
   TOAST NOTIFICATIONS
   ============================================ */

function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    const styles = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#22c55e' : '#3b82f6'};
        color: white;
        border-radius: 10px;
        font-weight: 600;
        z-index: 1000;
        animation: slideInFromRight 0.3s ease-out;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    `;
    
    Object.assign(toast.style, {
        position: 'fixed',
        bottom: '2rem',
        right: '2rem',
        padding: '1rem 1.5rem',
        background: type === 'success' ? '#22c55e' : '#3b82f6',
        color: 'white',
        borderRadius: '10px',
        fontWeight: '600',
        zIndex: '1000',
        boxShadow: '0 10px 25px rgba(0, 0, 0, 0.3)',
        animation: 'slideInFromRight 0.3s ease-out'
    });
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease-out forwards';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

/* ============================================
   SCROLL ANIMATIONS
   ============================================ */

function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .section-title').forEach(el => {
        observer.observe(el);
    });
}

/* ============================================
   QUANTITY CONTROLS
   ============================================ */

function updateQuantity(productId, change) {
    const qtyInput = document.getElementById(`qty-${productId}`);
    if (!qtyInput) return;

    let currentQty = parseInt(qtyInput.value) || 1;
    let newQty = currentQty + change;

    if (newQty < 1) newQty = 1;
    if (newQty > 99) newQty = 99;

    qtyInput.value = newQty;
    updateCartItem(productId, newQty);
}

function updateCartItem(productId, quantity) {
    // Store in localStorage for persistence
    let cart = JSON.parse(localStorage.getItem('cart') || '{}');
    
    if (quantity <= 0) {
        delete cart[productId];
    } else {
        cart[productId] = quantity;
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    
    // Recalculate totals
    recalculateTotal();
}

function recalculateTotal() {
    const items = document.querySelectorAll('.cart-item');
    let total = 0;

    items.forEach(item => {
        const priceStr = item.querySelector('.cart-item-price').textContent.replace('$', '');
        const price = parseFloat(priceStr);
        const qty = parseInt(item.querySelector('.cart-item-quantity input').value) || 1;
        total += price * qty;
    });

    const totalElement = document.querySelector('.summary-row.total .value');
    if (totalElement) {
        totalElement.textContent = `$${total.toFixed(2)}`;
    }
}

/* ============================================
   FORM VALIDATION
   ============================================ */

function validateCheckoutForm() {
    const inputs = document.querySelectorAll('.form-input');
    let isValid = true;

    inputs.forEach(input => {
        input.classList.remove('error');
        
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('error');
            showError(input, 'This field is required');
        } else if (input.type === 'email' && !isValidEmail(input.value)) {
            isValid = false;
            input.classList.add('error');
            showError(input, 'Please enter a valid email');
        }
    });

    return isValid;
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showError(input, message) {
    let errorEl = input.nextElementSibling;
    if (!errorEl || !errorEl.classList.contains('error-message')) {
        errorEl = document.createElement('div');
        errorEl.className = 'error-message';
        input.parentNode.insertBefore(errorEl, input.nextSibling);
    }
    errorEl.textContent = message;
}

/* ============================================
   SMOOTH SCROLL FOR INTERNAL LINKS
   ============================================ */

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

/* ============================================
   KEYBOARD SHORTCUTS
   ============================================ */

document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.getElementById('search');
        if (searchInput) {
            searchInput.focus();
        }
    }
});

/* ============================================
   MOBILE MENU (IF NEEDED)
   ============================================ */

function toggleMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks) {
        navLinks.classList.toggle('mobile-active');
    }
}