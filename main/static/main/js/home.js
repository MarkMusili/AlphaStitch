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