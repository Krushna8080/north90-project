document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');
    
    function toggleSidebar() {
        sidebar.classList.toggle('active');
        menuToggle.classList.toggle('shifted');
        mainContent.classList.toggle('shifted');
        menuToggle.textContent = sidebar.classList.contains('active') ? '×' : '☰';
    }
    
    menuToggle.addEventListener('click', function(e) {
        e.stopPropagation();
        toggleSidebar();
    });

    // Close sidebar when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInside = sidebar.contains(event.target) || menuToggle.contains(event.target);
        
        if (!isClickInside && sidebar.classList.contains('active')) {
            toggleSidebar();
        }
    });

    // Prevent sidebar closing when clicking inside it
    sidebar.addEventListener('click', function(e) {
        e.stopPropagation();
    });

    // Function to handle page zoom based on screen width
    function handlePageZoom() {
        const width = window.innerWidth;
        const body = document.body;

        if (width >= 992 && width <= 1600) {
            body.style.transform = 'scale(0.9)';
            body.style.width = '111.11%'; // Compensate for scale
        } else if (width >= 700 && width <= 767) {
            body.style.transform = 'scale(0.8)';
            body.style.width = '125%'; // Compensate for scale
        } else if (width > 600 && width < 700) {
            body.style.transform = 'scale(0.75)';
            body.style.width = '133.33%'; // Compensate for scale
        } else if (width <= 600) {
            body.style.transform = 'scale(0.5)';
            body.style.width = '200%'; // Compensate for scale
        } else {
            body.style.transform = 'scale(1)';
            body.style.width = '100%';
        }

        // Adjust container height after zoom
        const container = document.querySelector('.container');
        container.style.minHeight = `calc((100vh - 120px) / ${getComputedStyle(body).transform.split(',')[0].slice(7)})`;
    }

    // Initial zoom check
    handlePageZoom();

    // Handle window resize with debounce
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            handlePageZoom();
            if (window.innerWidth <= 600 && sidebar.classList.contains('active')) {
                toggleSidebar();
            }
        }, 250);
    });
});