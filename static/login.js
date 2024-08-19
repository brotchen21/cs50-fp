document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var message = document.getElementById("message");

    if (username === "admin" && password === "password") {
      message.style.color = "green";
      message.textContent = "Login successful!";
      window.location.href = "index.html";
    } else {
      message.style.color = "red";
      message.textContent = "Invalid username or password.";
    }
  });
