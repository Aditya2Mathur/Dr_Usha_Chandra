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
});
