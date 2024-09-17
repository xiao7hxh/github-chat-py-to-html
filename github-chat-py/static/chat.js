document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const question = document.getElementById('question').value;
    const chatBox = document.getElementById('chat-box');

    // Append user's question to the chat box
    chatBox.innerHTML += `<div class="message user"><div class="content">${question}</div></div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send request to the server
    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        // Append assistant's response to the chat box
        chatBox.innerHTML += `<div class="message assistant"><div class="content">${data.response}</div></div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
        document.getElementById('question').value = '';
    })
    .catch(error => console.error('Error:', error));
});
