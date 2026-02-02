/**
 * Heart Health Predictor - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function(tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add animation to elements when they come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 50) {
                const animationClass = element.dataset.animation || 'fadeIn';
                element.classList.add('animate__animated', `animate__${animationClass}`);
                element.classList.remove('animate-on-scroll');
            }
        });
    };

    // Run animation check on load and scroll
    animateOnScroll();
    window.addEventListener('scroll', animateOnScroll);

    // Add hover effect to cards
    const cards = document.querySelectorAll('.hover-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('shadow');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('shadow');
        });
    });

    // Form field dependencies (show/hide fields based on other selections)
    const setupFormDependencies = function() {
        // Example: If we have a field that should only show based on another selection
        const triggerFields = document.querySelectorAll('[data-trigger-field]');
        
        triggerFields.forEach(field => {
            field.addEventListener('change', function() {
                const targetSelector = this.dataset.targetField;
                const targetValue = this.dataset.targetValue;
                const targetField = document.querySelector(targetSelector);
                
                if (targetField) {
                    const targetContainer = targetField.closest('.form-group');
                    if (this.value === targetValue) {
                        targetContainer.classList.remove('d-none');
                    } else {
                        targetContainer.classList.add('d-none');
                    }
                }
            });
            
            // Trigger on load
            field.dispatchEvent(new Event('change'));
        });
    };
    
    setupFormDependencies();
});

/**
 * Show loading spinner when form is submitted
 */
const heartForm = document.getElementById('heart-form');
if (heartForm) {
    heartForm.addEventListener('submit', function() {
        if (this.checkValidity()) {
            const submitBtn = this.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Analyzing...';
            submitBtn.disabled = true;
        }
    });
} 