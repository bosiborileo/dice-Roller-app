const chatbotMessages = document.getElementById('chatbot-messages');
const chatbotText = document.getElementById('chatbot-text');
const chatbotSend = document.getElementById('chatbot-send');

chatbotSend.addEventListener('click', () => {
    const userMessage = chatbotText.value;
    const chatbotMessage = 'This is a sample response from the chatbot.';

    const userMessageElement = document.createElement('div');
    userMessageElement.classList.add('user-message');
    userMessageElement.textContent = userMessage;

    const chatbotMessageElement = document.createElement('div');
    chatbotMessageElement.classList.add('chatbot-message');
    chatbotMessageElement.textContent = chatbotMessage;

    chatbotMessages.appendChild(userMessageElement);
    chatbotMessages.appendChild(chatbotMessageElement);

    chatbotText.value = '';
});
