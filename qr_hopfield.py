import numpy as np
import matplotlib.pyplot as plt

# Función de activación (signo)
def sign(x):
    return np.where(x >= 0, 1, -1)

# Red de Hopfield
class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train_hebb(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)
        np.fill_diagonal(self.weights, 0)
        self.weights /= len(patterns)

    def recall(self, pattern, steps=5):
        s = pattern.copy()
        for _ in range(steps):
            s = sign(np.dot(self.weights, s))
        return s

# Crea un "QR" binarizado simple en 10x10 (1 = blanco, -1 = negro)
qr_original = np.array([
    [1,-1,-1,-1,-1,-1,-1,-1,-1, 1],
    [-1,1,1,1,1,1,1,1,1,-1],
    [-1,1,-1,-1,-1,-1,-1,-1,1,-1],
    [-1,1,-1,1,1,1,1,-1,1,-1],
    [-1,1,-1,1,-1,-1,1,-1,1,-1],
    [-1,1,-1,1,1,1,1,-1,1,-1],
    [-1,1,-1,-1,-1,-1,-1,-1,1,-1],
    [-1,1,1,1,1,1,1,1,1,-1],
    [1,-1,-1,-1,-1,-1,-1,-1,-1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Convertimos a vector 1D y binarizamos
pattern = qr_original.flatten()

# Creamos una copia ruidosa del QR
noisy_qr = pattern.copy()
noisy_qr[12] *= -1  # Invertimos un píxel
noisy_qr[77] *= -1
noisy_qr[88] *= -1

# Inicializamos y entrenamos la red
net = HopfieldNetwork(size=100)
net.train_hebb([pattern])

# Recuperamos la imagen
recovered_qr = net.recall(noisy_qr)

# Función para mostrar la imagen
def show_image(data, title):
    plt.imshow(data.reshape((10,10)), cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Mostrar y guardar QR original
show_image(pattern, "QR Original")
plt.savefig("qr_original.png")

# Mostrar y guardar QR con ruido
show_image(noisy_qr, "QR con Ruido")
plt.savefig("qr_ruido.png")

# Mostrar y guardar QR recuperado
show_image(recovered_qr, "QR Recuperado por Hopfield")
plt.savefig("qr_recuperado.png")

