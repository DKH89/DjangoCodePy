document.addEventListener("DOMContentLoaded", function () {
    const enviarCodigoBtn = document.getElementById('enviarCodigo');
    const codigoEstudiante = document.getElementById('codigoEstudiante');
    const descripcionEjercicio = document.querySelector('.descripcion-ejercicio').innerText;
    const modal = document.getElementById('modalCorrecciones');
    const closeModalBtn = document.querySelector('.close');
    const correccionesTexto = document.getElementById('correccionesTexto');
    const correccionesEstado = document.getElementById('CorreccionesEstado'); // Nuevo elemento para cambiar el texto

    enviarCodigoBtn.addEventListener('click', function () {
        const codigoUsuario = codigoEstudiante.innerText;

        console.log(codigoUsuario);

        if (codigoUsuario.trim() === '') return;

        const mensajeChatGPT = 
        `CORRIJA ESTE EJERCICIO , LAS CORRECIONES LAS DEBE HACER EN VIÑETAS SI ES EL CASO , NO DECIR AQUI TIENES LAS CORRECIONES PARA EL EJERCICIO PROPUESTO NI NADA PARECIDO NI TAMPOCO EL CODIGO PROPORCIONADO POR EL USUARIO ,SOLO MUESTRE EL MENSAJE CON CORRECIONES Y YA , NO MUESTRE EL CODIGO YA CORREGIDO NI LA IMPLEMENTACIÓN CORRECTA , DE CORRECIONES ESPECIFICAS Y POSIBLES EJEMPLOS QUE PUEDEN SERVIR PARA SOLUCIONAR DICHO ERROR, EN CASO DE QUE LO QUE ESCRIBIO EL USUARIO ESTE BIEN ANALICE QUE LE FALTA PARA COMPLETAR CON LA DESCRIPCIÓN DEL EJERCICIO PROPUESTO SI ES EL CASO ,SI TODO ESTA CORRECTO DIGA "APROBADO" ` +
        `EL EJERCICIO QUE SE DEBE HACER ES ESTE: "${descripcionEjercicio}". ` +
        `Y LO QUE EL USUARIO ENVIO ES ESTO: (RECUERDE DECIR APROBADO SI TODO ESTA BIEN Y CUMPLE CON TODO) "${codigoUsuario}".`;

        console.log(mensajeChatGPT); // Imprimir el código en la consola
        const csrfToken = getCookie('csrftoken');

        $.ajax({
            url: "/InteligenciaArtificial/",
            type: "POST",
            headers: { "X-CSRFToken": csrfToken },
            data: { user_input: mensajeChatGPT },
            success: function(data) {
                // Reemplazar viñetas por un salto de línea HTML para mayor orden
                let formattedResponse = data.response.replace(/-/g, '<br>•');
                correccionesTexto.innerHTML = `<p>${formattedResponse}</p>`; // Muestra el mensaje de la IA

                // Verificar si la respuesta incluye "APROBADO" y cambiar el texto del elemento
                if (formattedResponse.includes("APROBADO")) {
                    correccionesEstado.innerText = "APROBADO"; // Cambiar texto a "APROBADO"
                } else {
                    correccionesEstado.innerText = "e"; // O el texto que desees por defecto
                }

                // Mostrar el modal
                modal.style.display = 'block';
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log("Error en la solicitud AJAX:", errorThrown);
            }
        });

    });

    // Cerrar el modal cuando el usuario haga clic en la "X"
    closeModalBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Cerrar el modal si el usuario hace clic fuera del modal
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
