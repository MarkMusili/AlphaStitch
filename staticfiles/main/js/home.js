document.addEventListener("DOMContentLoaded", function() {
    // Function to initialize carousel with touch and dot navigation
    function initializeCarousel(listClass, prevButtonId, nextButtonId, itemClass, dotContainerId) {
        const list = document.querySelector(`.${listClass}`);
        const prevButton = document.getElementById(prevButtonId);
        const nextButton = document.getElementById(nextButtonId);
        const dotContainer = document.getElementById(dotContainerId);
        const items = document.querySelectorAll(`.${itemClass}`);
        const itemWidth = items[0].offsetWidth; // Width of each item
        let currentSlide = 0;
        const totalItems = items.length;
        let startX, endX;
        const minSwipeDistance = 50; // Minimum distance for it to be considered a swipe

        if (list && prevButton && nextButton && dotContainer && items.length) {
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
                dots.forEach(dot => dot.classList.remove('active'));
                if (dots[currentSlide]) dots[currentSlide].classList.add('active');
            }

            // Event listeners for next and prev buttons
            prevButton.onclick = function() {
                currentSlide = (currentSlide === 0) ? totalItems - 1 : currentSlide - 1;
                updateCarousel();
            };

            nextButton.onclick = function() {
                currentSlide = (currentSlide === totalItems - 1) ? 0 : currentSlide + 1;
                updateCarousel();
            };

            // Swipe functionality with a threshold for minimum swipe distance
            list.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX; // Get the initial touch position
            });

            list.addEventListener('touchmove', (e) => {
                endX = e.touches[0].clientX; // Update the position as the finger moves
            });

            list.addEventListener('touchend', () => {
                let swipeDistance = startX - endX;

                // Only consider a swipe if the distance is greater than the minimum swipe threshold
                if (Math.abs(swipeDistance) > minSwipeDistance) {
                    // Swipe left (next item)
                    if (swipeDistance > 0 && currentSlide < totalItems - 1) {
                        currentSlide++;
                    }
                    // Swipe right (previous item)
                    else if (swipeDistance < 0 && currentSlide > 0) {
                        currentSlide--;
                    }

                    updateCarousel();
                }
            });

            // Initialize carousel display
            updateCarousel();
        } else {
            console.error(`One or more elements not found for ${listClass}`);
        }
    }

    // Initialize carousels with dot and touch navigation
    initializeCarousel('product_list', 'prev', 'next', 'product_item', 'dot-navigation');
});
