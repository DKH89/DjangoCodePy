document.addEventListener("DOMContentLoaded", function () {
    const codigoEstudiante = document.getElementById('codigoEstudiante');
    const palabrasClave = ["if", "else", "for", "while", "input", "return", "def","input","int", "class", "import", "from", "try", "except", "finally", "with", "as", "yield", "break", "continue", "pass", "elif", "in", "print", "="];

    function guardarPosicionCursor() {
        const selection = window.getSelection();
        if (selection.rangeCount > 0) {
            const range = selection.getRangeAt(0);
            const preCaretRange = range.cloneRange();
            preCaretRange.selectNodeContents(codigoEstudiante);
            preCaretRange.setEnd(range.endContainer, range.endOffset);
            return preCaretRange.toString().length;
        }
        return 0;
    }

    function restaurarPosicionCursor(posicion) {
        const selection = window.getSelection();
        const nodes = codigoEstudiante.childNodes;
        let charCount = 0, node;

        for (let i = 0; i < nodes.length; i++) {
            node = nodes[i];
            if (node.nodeType === Node.TEXT_NODE) {
                if (charCount + node.length >= posicion) {
                    const range = document.createRange();
                    range.setStart(node, posicion - charCount);
                    range.collapse(true);
                    selection.removeAllRanges();
                    selection.addRange(range);
                    return;
                } else {
                    charCount += node.length;
                }
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                const textLength = node.innerText.length;
                if (charCount + textLength >= posicion) {
                    for (let j = 0; j < node.childNodes.length; j++) {
                        const innerNode = node.childNodes[j];
                        const innerLength = innerNode.nodeValue ? innerNode.nodeValue.length : 0;
                        if (charCount + innerLength >= posicion) {
                            const range = document.createRange();
                            range.setStart(innerNode, posicion - charCount);
                            range.collapse(true);
                            selection.removeAllRanges();
                            selection.addRange(range);
                            return;
                        }
                        charCount += innerLength;
                    }
                } else {
                    charCount += textLength;
                }
            }
        }
    }

    codigoEstudiante.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            const textoActual = codigoEstudiante.innerHTML;

            if (!textoActual.endsWith('<br><br>')) {
                document.execCommand('insertHTML', false, '<br><br>');
            }

            const range = document.createRange();
            const selection = window.getSelection();
            range.setStart(codigoEstudiante, codigoEstudiante.childNodes.length);
            range.collapse(true);
            selection.removeAllRanges();
            selection.addRange(range);
        }

        if (event.key === 'Tab') {
            event.preventDefault();
            const espacios = "  ";
            const posicionCursor = guardarPosicionCursor();
            document.execCommand('insertHTML', false, espacios);
            restaurarPosicionCursor(posicionCursor + espacios.length);
        }

        if (event.key === ' ') {
            event.stopPropagation();
            const posicionCursor = guardarPosicionCursor();
            document.execCommand('insertHTML', false, ' ');
            restaurarPosicionCursor(posicionCursor + 1);
            event.preventDefault();
        }
    });

    codigoEstudiante.addEventListener('input', function () {
        const posicionCursor = guardarPosicionCursor();

        const textoOriginal = codigoEstudiante.innerText;

        // Ajustar la división para detectar palabras clave dentro de expresiones como print(x)
        const palabras = textoOriginal.split(/(\b|\s+)/);

        let nuevoContenido = '';
        palabras.forEach(function (palabra) {
            // Usamos una expresión regular para detectar palabras clave rodeadas de otros caracteres
            const palabraLimpia = palabra.replace(/[^\w]/g, '');  // Eliminar caracteres no alfabéticos
            if (palabrasClave.includes(palabraLimpia)) {
                nuevoContenido += `<span class="palabra-clave">${palabra}</span>`;
            } else {
                nuevoContenido += palabra;
            }
        });

        // Actualizar solo si el contenido ha cambiado, para evitar pérdida del cursor innecesariamente
        if (codigoEstudiante.innerHTML !== nuevoContenido) {
            codigoEstudiante.innerHTML = nuevoContenido;
            restaurarPosicionCursor(posicionCursor);
        }
    });
});
