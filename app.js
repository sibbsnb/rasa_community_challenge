$(document).ready(function () {
    var chatContainer = $('#chat-container');
    var userInput = $('#user-input');
    var sendButton = $('#send-btn');

    // Function to add a user message to the chat container
    function addUserMessage(message) {
        chatContainer.append('<div class="user-message"><span class="user-icon"><i class="fas fa-user"></i></span>' + message + '</div>');
    }

    // Function to add a bot message to the chat container
    function addBotMessage(message) {
        chatContainer.append('<div class="bot-message"><span class="bot-icon"><i class="fas fa-robot"></i></span>' + message + '</div>');
    }

    // Function to send user input to the Rasa server
    function sendMessage() {
        var userMessage = userInput.val();
        addUserMessage(userMessage);

        // Make a POST request to the Rasa server API
        $.ajax({
            url: 'http://localhost:5005/webhooks/rest/webhook',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                sender: 'user',
                message: userMessage
            }),
            success: function (data) {
                if (data && data.length > 0) {
                    data.forEach(element => {
                        var botResponse = element.text;
                        addBotMessage(botResponse);
                    });
                    //var botResponse = data[0].text;
                    //addBotMessage(botResponse);
                }
            },
            error: function () {
                addBotMessage('Oops! Something went wrong. Please try again.');
            }
        });

        // Clear the user input field after sending the message
        userInput.val('');
    }

    // Bind event listener to the send button
    sendButton.on('click', function () {
        sendMessage();
    });

    // Bind event listener to the user input field to handle "Enter" key press
    userInput.on('keyup', function (event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});
