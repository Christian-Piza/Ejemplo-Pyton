import numpy as np

# Datos empresariales: por ejemplo, ventas por canal A, B y C durante varios meses
# Filas: meses, Columnas: canales de venta
ventas = np.array([
    [100, 80, 90],
    [120, 95, 100],
    [130, 100, 105],
    [150, 120, 115]
])

# Centrado de los datos (como en PCA)
ventas_centradas = ventas - np.mean(ventas, axis=0)

# Transponemos para aplicar Gram-Schmidt a los vectores columna (variables)
def gram_schmidt(X):
    Q = []
    for v in X.T:  # Vectores columna
        for q in Q:
            v = v - np.dot(q, v) * q
        v = v / np.linalg.norm(v)
        Q.append(v)
    return np.array(Q).T  # Regresamos a forma de matriz

# Obtener base ortonormal
base_ortonormal = gram_schmidt(ventas_centradas)

print("Base ortonormal a partir de los datos de ventas:")
print(base_ortonormal)

# Verificamos si la matriz es ortogonal
print("¿Es ortogonal? Qᵀ·Q = I")
print(np.allclose(base_ortonormal.T @ base_ortonormal, np.identity(base_ortonormal.shape[1])))

