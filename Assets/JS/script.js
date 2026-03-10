document.addEventListener('DOMContentLoaded', () => {    // 2. Mobile Menu Toggle Logic
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    // Toggle active class on button and navigation
    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        mainNav.classList.toggle('active');
        
        // Transform hamburger icon to close (X) icon when active
        const icon = mobileMenuToggle.querySelector('i');
        if (mobileMenuToggle.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-xmark');
        } else {
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        }
    });

    // Close mobile menu when a navigation link is clicked
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 991) {
                mobileMenuToggle.classList.remove('active');
                mainNav.classList.remove('active');
                const icon = mobileMenuToggle.querySelector('i');
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    });

    // Smooth Scrolling for Anchor Links (Removed for Multi-Page layout)

    // 4. Contact Form Google Sheets Integration
    const scriptURL = 'https://script.google.com/macros/s/AKfycbxuJS5tw1XMlpvaw75KA5jw0nwz-i3JqUnDvRlTYmD_MsVXZ53A5PFYTT_CWnrjfMMC/exec'; // Replace this URL!
    const form = document.getElementById('appointmentForm');
    const submitBtn = document.getElementById('submitBtn');
    const formMessage = document.getElementById('formMessage');

    if (form) {
        form.addEventListener('submit', e => {
            e.preventDefault();
            
            // Show loading state
            submitBtn.disabled = true;
            submitBtn.innerText = 'Submitting...';
            formMessage.style.display = 'none';

            // Gather data
            let requestBody = new FormData(form);

            fetch(scriptURL, { method: 'POST', body: requestBody })
                .then(response => {
                    formMessage.style.display = 'block';
                    formMessage.style.color = '#532c1f'; // Primary Green / Brown
                    formMessage.innerText = 'Thank you! Your request has been submitted successfully.';
                    submitBtn.disabled = false;
                    submitBtn.innerText = 'Submit Request';
                    form.reset();
                })
                .catch(error => {
                    console.error('Error!', error.message);
                    formMessage.style.display = 'block';
                    formMessage.style.color = 'red';
                    formMessage.innerText = 'Oops! Something went wrong. Please try again later.';
                    submitBtn.disabled = false;
                    submitBtn.innerText = 'Submit Request';
                });
        });
    }

    // 5. Before & After Slider Logic
    document.querySelectorAll('.ba-slider').forEach(slider => {
        slider.addEventListener('input', (e) => {
            const val = e.target.value;
            const container = e.target.parentElement;
            container.querySelector('.img-before').style.clipPath = `inset(0 ${100 - val}% 0 0)`;
            container.querySelector('.ba-divider').style.left = `${val}%`;
        });
    });

    // 6. Dynamic AOS Animations & Background Shapes injection
    // Add AOS attributes to key elements for scroll animations
    document.querySelectorAll('.hero-subtitle, .section-subtitle').forEach(el => el.setAttribute('data-aos', 'fade-up'));
    document.querySelectorAll('.hero-title, .section-title, .page-title').forEach((el) => {
        el.setAttribute('data-aos', 'fade-up');
        el.setAttribute('data-aos-delay', '100');
    });
    document.querySelectorAll('.hero-desc, .about-desc, .section-desc, .breadcrumb').forEach((el) => {
        el.setAttribute('data-aos', 'fade-up');
        el.setAttribute('data-aos-delay', '200');
    });
    document.querySelectorAll('.btn-primary, .hero-actions').forEach((el) => {
        el.setAttribute('data-aos', 'fade-up');
        el.setAttribute('data-aos-delay', '300');
    });
    document.querySelectorAll('.info-card, .service-card, .clinic-card, .team-member, .benefits-list li').forEach((el, index) => {
        el.setAttribute('data-aos', 'fade-up');
        el.setAttribute('data-aos-delay', (index % 3) * 100 + ''); 
    });
    document.querySelectorAll('.about-image-wrapper, .contact-form-wrapper').forEach(el => {
        el.setAttribute('data-aos', 'fade-right');
    });
    document.querySelectorAll('.doc-image-wrapper, .features-image img, .ba-container').forEach(el => {
        el.setAttribute('data-aos', 'fade-left');
    });

    // Inject animated background floating shapes to each section
    const animatedShapesHTML = `
        <svg class="bg-shape shape-flower shape-1" width="45" height="45" viewBox="0 0 24 24" fill="var(--primary-green)">
            <path d="M12,2 C14,5 18,8 22,8 C18,8 14,11 12,14 C10,11 6,8 2,8 C6,8 10,5 12,2 Z" />
            <path d="M12,10 C14,13 18,16 22,16 C18,16 14,19 12,22 C10,19 6,16 2,16 C6,16 10,13 12,10 Z" transform="rotate(45 12 12)" />
        </svg>
        <svg class="bg-shape shape-leaf shape-2" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--primary-green)" stroke-width="2">
            <path d="M12 2C8 2 4 6 4 12c0 6 8 10 8 10s8-4 8-10C20 6 16 2 12 2z" />
        </svg>
        <svg class="bg-shape shape-dots shape-3" width="50" height="50" viewBox="0 0 24 24" fill="var(--primary-green)">
            <circle cx="4" cy="4" r="2" />
            <circle cx="12" cy="4" r="2" />
            <circle cx="20" cy="4" r="2" />
            <circle cx="4" cy="12" r="2" />
            <circle cx="12" cy="12" r="2" />
            <circle cx="20" cy="12" r="2" />
            <circle cx="4" cy="20" r="2" />
            <circle cx="12" cy="20" r="2" />
            <circle cx="20" cy="20" r="2" />
        </svg>
    `;
    
    document.querySelectorAll('section:not(.hero):not(.quick-info), .page-banner').forEach(section => {
        // Only inject into sections that don't already have background animations
        if (!section.querySelector('.bg-shape')) {
            section.style.position = 'relative';
            section.style.overflow = 'hidden';
            section.insertAdjacentHTML('afterbegin', animatedShapesHTML);
        }
    });

    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 50,
        });
    }

});
