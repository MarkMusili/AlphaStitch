document.addEventListener("DOMContentLoaded", function() {
    const searchContainer = document.getElementById('search-container');
    const overlay = document.getElementById('overlay');
    const searchInput = document.getElementById('search-input');
    const suggestionsBox = document.getElementById('suggestions-box');

    // Show search bar and overlay when the search icon is clicked
    document.getElementById('open-search').addEventListener('click', function() {
        searchContainer.classList.remove('hidden'); // Show the search bar
        overlay.style.display = 'block'; // Show the overlay
        searchInput.focus(); // Focus on the search input
    });

    // Hide search bar and overlay when the close button or overlay is clicked
    document.getElementById('close-search').addEventListener('click', function() {
        searchContainer.classList.add('hidden'); // Hide the search bar
        overlay.style.display = 'none'; // Hide the overlay
        searchContainer.classList.remove('suggestions-visible'); // Remove the border-radius change
    });

    // Close when clicking on the overlay
    overlay.addEventListener('click', function() {
        searchContainer.classList.add('hidden'); // Hide the search bar
        this.style.display = 'none'; // Hide the overlay
        searchContainer.classList.remove('suggestions-visible'); // Remove the border-radius change
    });

    searchInput.addEventListener('keyup', function() {
        let query = this.value;

        if (query.length > 0) {
            fetch(`/search_suggestions/?query=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = "";
                    if (data.length > 0) {
                        suggestionsBox.style.display = "block";
                        searchContainer.classList.add('suggestions-visible'); // Add the border-radius change
                        let ul = document.createElement('ul');
                        data.forEach(item => {
                            let li = document.createElement('li');
                            li.textContent = `${item.name}`;
                            li.addEventListener('click', () => {
                                window.location.href = item.url;
                            });
                            ul.appendChild(li);
                        });
                        suggestionsBox.appendChild(ul);
                    } else {
                        suggestionsBox.style.display = "none";
                        searchContainer.classList.remove('suggestions-visible'); // Remove the border-radius change
                    }
                });
        } else {
            suggestionsBox.style.display = "none";
            searchContainer.classList.remove('suggestions-visible'); // Remove the border-radius change
        }
    });

});