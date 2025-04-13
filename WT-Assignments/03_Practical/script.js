document.getElementById("registrationForm").addEventListener("submit", function(event) {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let dob = document.getElementById("dob").value;
    let errorMessage = document.getElementById("errorMessage");

    if (!email.includes("@")) {
        errorMessage.textContent = "Invalid email address!";
        event.preventDefault();
    } else if (password.length < 6) {
        errorMessage.textContent = "Password must be at least 6 characters!";
        event.preventDefault();
    } else {
        errorMessage.textContent = "";
        alert("Registration successful!");
    }
});
