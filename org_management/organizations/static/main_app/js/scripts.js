// Confirm before deleting an organization or user
document.addEventListener('DOMContentLoaded', () => {
    const deleteLinks = document.querySelectorAll('a[href*="delete"]');

    deleteLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            const confirmDelete = confirm("Are you sure you want to delete this item?");
            if (!confirmDelete) {
                event.preventDefault(); // Prevent the default action if the user cancels
            }
        });
    });
});

// Form validation for role assignment
document.addEventListener('DOMContentLoaded', () => {
    const roleForm = document.querySelector('form[action*="assign_role"]');

    if (roleForm) {
        roleForm.addEventListener('submit', (event) => {
            const roleSelect = roleForm.querySelector('select[name="role"]');
            
            if (!roleSelect.value) {
                alert("Please select a role before submitting.");
                event.preventDefault(); // Prevent form submission
            }
        });
    }
});

// Toggle visibility of elements (example: extra form fields)
function toggleVisibility(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = element.style.display === 'none' ? 'block' : 'none';
    }
}
