document.querySelector(".login-form").addEventListener("submit", function(e) {
    e.preventDefault();
  
    // Get the input values
    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;
  
    // Check if the username and password are 'admin'
    if (username === "admin" && password === "admin") {
      // Redirect to the dashboard page (dashboard.html)
      window.location.href = 'dashboard.html';  // Redirect to the dashboard page after successful login
    } else {
      // Display an error message if login fails
      const errorMessage = document.querySelector("#error-message");
      errorMessage.textContent = "Invalid username or password.";
      errorMessage.style.display = "block";
    }
  });
  