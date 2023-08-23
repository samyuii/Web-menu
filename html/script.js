document.addEventListener("DOMContentLoaded", function () {
    const menu = document.getElementById("menu");
    const output = document.getElementById("output");

    // Function to display output
    function displayOutput(message) {
        output.innerHTML = message;
    }

    // Function to execute an action using AJAX
    function executeAction(action) {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "cgi-bin/backend.py?action=${action}", true);

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    displayOutput(xhr.responseText);
                } else {
                    displayOutput("Error occurred while executing action.");
                }
            }
        };

        xhr.send();
    }

    // Event listeners for menu buttons
    menu.addEventListener("click", function (event) {
        const button = event.target;
        if (button.id === "send-message") {
            executeAction("send_message");
        } else if (button.id === "open-app-menu") {
            executeAction("open_app_menu");
        } else if (button.id === "other-options") {
            executeAction("other_options");
        }
    });
});

