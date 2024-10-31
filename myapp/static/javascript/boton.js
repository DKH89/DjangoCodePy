
  document.getElementById('compilarCodigo').onclick = function() {
      // Verificar si el texto de las correcciones contiene la palabra "APROBADO"
      var correccionesTexto = document.getElementById('CorreccionesEstado').innerText; // Cambiar 'correccionesEstado' a 'CorreccionesEstado'

      // Comprobar si el texto es "APROBADO" (sin importar mayúsculas o minúsculas)
      if (correccionesTexto.toUpperCase() === 'APROBADO') {
          // Si está aprobado, proceder a compilar el código
          var codigo = document.getElementById('codigoEstudiante').innerText;
          var codigoCodificado = encodeURIComponent(codigo);
          var urlCompilador = `https://paiza.io/es/projects/new?language=python3&source_code=${codigoCodificado}`;
          window.open(urlCompilador, '_blank');
      } else {
          // Si no está aprobado, mostrar un mensaje de error
          alert('Debes corregir el código antes de compilar.');
      }
  };
