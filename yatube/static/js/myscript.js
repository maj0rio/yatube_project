window.addEventListener('DOMContentLoaded', function() {
    var accountLink = document.querySelector('#account-link');
    var accountDropdown = document.querySelector('#account-dropdown');

    accountLink.addEventListener('mouseover', function() {
        accountDropdown.style.display = 'block';
    });

    accountDropdown.addEventListener('mouseleave', function() {
        accountDropdown.style.display = 'none';
    });
});