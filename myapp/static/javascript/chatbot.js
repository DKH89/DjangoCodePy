
document.addEventListener("DOMContentLoaded", function () {
    const chatIcon = document.getElementById('chatIcon');
    const chatBox = document.getElementById('chatBox');
    const closeChat = document.getElementById('closeChat');
    const userInput = document.getElementById('userInput');
    const chatContent = document.getElementById('chatContent');
    const sendMessageBtn = document.getElementById('sendMessage');

    chatIcon.addEventListener('click', function () {
        chatBox.style.display = 'block';
    });

    closeChat.addEventListener('click', function () {
        chatBox.style.display = 'none';
    });

    sendMessageBtn.addEventListener('click', function () {
        const userMessage = userInput.value;
        if (userMessage.trim() === '') return;

        appendMessage(userMessage, 'user');

        // Obtener el token CSRF del documento
        const csrfToken = getCookie('csrftoken');
        
        // Realizar la solicitud AJAX al servidor incluyendo el token CSRF
        $.ajax({
            url: "/InteligenciaArtificial/",
            type: "POST",
            headers: { "X-CSRFToken": csrfToken },
            data: { user_input: userMessage },
            // En la función success de la solicitud AJAX
            success: function(data) {
                appendMessage(data.response, 'bot'); // Agregar la respuesta del chatbot al chat
                chatContent.scrollTop = chatContent.scrollHeight;
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log("Error en la solicitud AJAX:", errorThrown);
            }
        });

        userInput.value = '';
    });

    function appendMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);
        messageElement.innerText = message;
        chatContent.appendChild(messageElement);
        chatContent.scrollTop = chatContent.scrollHeight;
    }

    // Definir la función para obtener el valor del token CSRF de Django
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Obtener el valor del token CSRF si el nombre coincide
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});