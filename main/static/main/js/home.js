document.addEventListener("DOMContentLoaded", function() {
    // Function to initialize carousel
    function initializeCarousel(listClass, prevButtonId, nextButtonId, itemClass) {
        const list = document.querySelector(`.${listClass}`);
        const prevButton = document.getElementById(prevButtonId);
        const nextButton = document.getElementById(nextButtonId);

        console.log(`Initializing carousel for ${listClass}`);
        console.log('List:', list);
        console.log('Prev Button:', prevButton);
        console.log('Next Button:', nextButton);

        if (list && prevButton && nextButton) {
            const item = document.querySelector(`.${itemClass}`);
            console.log('Item:', item);

            if (item) {
                const itemWidth = item.offsetWidth; // Full width of the item

                prevButton.onclick = function() {
                    console.log(`Prev button clicked for ${listClass}`);
                    list.scrollLeft -= itemWidth;
                };

                nextButton.onclick = function() {
                    console.log(`Next button clicked for ${listClass}`);
                    list.scrollLeft += itemWidth;
                };
            } else {
                console.error(`Item with class ${itemClass} not found`);
            }
        } else {
            console.error(`One or more elements not found for ${listClass}`);
        }
    }

    // Initialize carousels
    initializeCarousel('product_list', 'prev', 'next', 'product_item');
    initializeCarousel('review_list', 'reviews-prev', 'reviews-next', 'review_item');
});
document.addEventListener("DOMContentLoaded", function() {
    // Function to initialize carousel with dot navigation
    function initializeCarousel(listClass, prevButtonId, nextButtonId, itemClass, dotContainerId) {
        const list = document.querySelector(`.${listClass}`);
        const prevButton = document.getElementById(prevButtonId);
        const nextButton = document.getElementById(nextButtonId);
        const dotContainer = document.getElementById(dotContainerId);

        if (list && prevButton && nextButton && dotContainer) {
            const items = document.querySelectorAll(`.${itemClass}`);
            const itemWidth = items[0].offsetWidth; // Width of each item
            let currentSlide = 0;

            // Create dots for each item
            dotContainer.innerHTML = ''; // Clear any existing dots
            items.forEach((_, index) => {
                const dot = document.createElement('span');
                dot.classList.add('dot');
                if (index === 0) dot.classList.add('active'); // Set first dot as active
                dotContainer.appendChild(dot);

                // Add click event to each dot for navigation
                dot.addEventListener('click', () => {
                    currentSlide = index;
                    updateCarousel();
                });
            });

            const dots = dotContainer.querySelectorAll('.dot');

            // Function to update carousel display and active dot
            function updateCarousel() {
                list.scrollLeft = currentSlide * itemWidth;

                // Update active dot
                dots.forEach(dot => dot.classList.remove('active'));
                if (dots[currentSlide]) dots[currentSlide].classList.add('active');
            }

            // Event listeners for next and prev buttons
            prevButton.onclick = function() {
                currentSlide = (currentSlide === 0) ? items.length - 1 : currentSlide - 1;
                updateCarousel();
            };

            nextButton.onclick = function() {
                currentSlide = (currentSlide === items.length - 1) ? 0 : currentSlide + 1;
                updateCarousel();
            };

            // Initialize carousel display
            updateCarousel();
        } else {
            console.error(`One or more elements not found for ${listClass}`);
        }
    }

    // Initialize carousels with dot navigation
    initializeCarousel('product_list', 'prev', 'next', 'product_item', 'dot-navigation');
    // Initialize other carousels here if needed
});
