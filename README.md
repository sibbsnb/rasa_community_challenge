# Rasa Community Challenge - Performance Feedback Intelligence using Generative AI with Rasa

This project aims to provide an intelligent chatbot that can assist with performance feedback for employees using Generative AI with Rasa.

## Getting Started

### Replace the Open API token in `actions.py`

Before running the Rasa server, make sure to replace the Open API token in the `actions.py` file. This token is required to access the Generative AI API.

### Run Rasa Server

To run the Rasa server with the REST API enabled, use the following command:

```bash
rasa run --enable-api --cors "*" --port 5005 --debug
```

### Run Action Server

Start the action server for custom actions:

```bash
rasa run actions
```

### Chat with the Chatbot

Open `index.html` in a web browser to chat with the chatbot. The chatbot will provide performance feedback based on user input.

![Performance Bot Screenshot](path/to/your/performance bot screenshot.png)


---




