document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('groupsSearch');
    const grid = document.getElementById('groupsGrid');
    const noResults = document.getElementById('noResults');

    if (!searchInput || !grid) return;

    let timeout = null;

    function fetchGroups(query) {
        const url = new URL('/posts/groups/search/', window.location.origin);
        url.searchParams.append('q', query.trim());

        fetch(url, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            grid.innerHTML = data.html;
            if (noResults) {
                noResults.style.display = (data.count === 0) ? 'block' : 'none';
            }
        })
        .catch(error => console.error('Search error:', error));
    }

    searchInput.addEventListener('input', function () {
        clearTimeout(timeout);
        const query = this.value;
        timeout = setTimeout(() => {
            fetchGroups(query);
        }, 300); 
    });
});