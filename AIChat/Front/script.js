async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    const outputDiv = document.getElementById('output');
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = '你：' + userInput;
    outputDiv.appendChild(userMessage);

    // 发送用户输入到后端
    const response = await fetch('http://localhost:5000/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    });

    const data = await response.json();
    const aiMessage = document.createElement('div');
    aiMessage.className = 'message ai-message';
    aiMessage.textContent = "智能AI客服：" + data.response;
    outputDiv.appendChild(aiMessage);

    // 清空输入框
    document.getElementById('userInput').value = '';
    outputDiv.scrollTop = outputDiv.scrollHeight;
}