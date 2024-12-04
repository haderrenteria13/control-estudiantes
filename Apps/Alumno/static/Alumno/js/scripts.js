document.addEventListener('DOMContentLoaded', function () {
    var toggleBtn = document.querySelector('.toggle-btn');
    var sideNav = document.getElementById('side_nav');

    toggleBtn.addEventListener('click', function () {
        sideNav.classList.toggle('reduced');
    });
});