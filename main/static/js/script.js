document.addEventListener("DOMContentLoaded", function () {
    const loginButton = document.getElementById("loginButton");
    const dropdownMenu = document.getElementById("dropdownMenu");

    loginButton.addEventListener("click", function () {
        dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
    });

    document.addEventListener("click", function (event) {
        if (!event.target.closest('.login-dropdown')) {
            dropdownMenu.style.display = "none";
        }
    });
});
