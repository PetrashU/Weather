document.addEventListener('DOMContentLoaded', function () {
    const table = document.getElementById('mytable');
    const itemsPerPage = 5;
    let currentPage = 0;
    const rows = Array.from(table.querySelectorAll('tbody tr'));
  
    function showPage(page) {
        const startIndex = page * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;
        rows.forEach((row, index) => {
            row.style.display = index >= startIndex && index < endIndex ? '' : 'none';
        });
        updateActiveButtonStates();
    }
  
    function createPageButtons() {
        const totalPages = Math.ceil(rows.length / itemsPerPage);
        const paginationContainer = document.createElement('div');
        const paginationDiv = table.parentNode.appendChild(paginationContainer);
        paginationContainer.classList.add('pagination');
  
        for (let i = 0; i < totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.textContent = i + 1;
            pageButton.addEventListener('click', () => {
                currentPage = i;
                showPage(currentPage);
                updateActiveButtonStates();
            });
            paginationDiv.appendChild(pageButton);
        }
    }
  
    function updateActiveButtonStates() {
        const pageButtons = document.querySelectorAll('.pagination button');
        pageButtons.forEach((button, index) => {
            if (index === currentPage) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });
    }
  
    createPageButtons();
    showPage(currentPage);
});