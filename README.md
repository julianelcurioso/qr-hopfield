# qr-hopfield
Reconocimiento de imágenes ruidosas con red neuronal de Hopfield - TP3 Inteligencia Artificial
# Prototipo Hopfield QR - TP3 Inteligencia Artificial

Este proyecto presenta un prototipo de red neuronal artificial basado en el modelo de **Hopfield**, implementado en Python, aplicado a la recuperación de patrones visuales simplificados de tipo **código QR**.

# Objetivo

El prototipo fue desarrollado en el marco del **Trabajo Práctico 3** de la materia **Inteligencia Artificial** (Licenciatura en Informática - Universidad Siglo 21), cuyo objetivo es identificar patrones dañados o ruidosos a partir de una imagen binarizada. Se busca emular una posible solución industrial de bajo costo para validación de etiquetas QR en líneas de producción.

# ¿Qué hace este prototipo?

- Simula un QR simple en una grilla de 10x10 píxeles (blanco/negro).
- Entrena una red de Hopfield con ese patrón.
- Introduce ruido (errores en algunos píxeles).
- Recupera el patrón original mediante la red.
- Muestra imágenes del proceso con `matplotlib`.

# Imágenes generadas

Al ejecutar el script, se muestran 3 imágenes:
1. QR original
2. QR con ruido
3. QR recuperado por la red Hopfield

> También pueden ser guardadas automáticamente como PNG, si se requiere.

# Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/qr-hopfield.git
   cd qr-hopfield
