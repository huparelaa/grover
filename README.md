# Algoritmo de Grover
Este repositorio contiene una implementación del algoritmo de Grover utilizando Python y NumPy. El algoritmo de Grover es un algoritmo cuántico para la búsqueda no estructurada que puede encontrar un elemento marcado en una lista no ordenada con una complejidad cuadrática, mejorando significativamente la búsqueda clásica.

## Descripción del Algoritmo

El algoritmo de Grover aprovecha la superposición y el paralelismo cuántico para buscar un elemento en una base de datos no estructurada de tamaño \(N\) en raíz de \(N\)
 operaciones. Este es un avance significativo en comparación con los \(O(N)\) operaciones requeridas en una búsqueda clásica.

### Componentes Principales

1. **Matriz de Hadamard**: Esta matriz se usa para crear una superposición uniforme de todos los estados posibles.
2. **Producto Tensorial**: Utilizado para expandir la matriz de Hadamard a múltiples qubits.
3. **Matriz de Identidad**: Utilizada para construir operadores de difusión y oráculos.
4. **Operador de Difusión**: Incrementa las amplitudes de los estados objetivo.
5. **Oráculo**: Identifica el estado objetivo invertiendo su amplitud.
6. **Iteraciones de Grover**: Aplicación repetida del oráculo y el operador de difusión para amplificar la probabilidad del estado objetivo.

### ¿Cómo correr el código?

1. Clona este repositorio.
2. Asegúrate de tener Python y NumPy instalados. Puedes instalar NumPy usando el comando `pip install numpy`.
3. Ejecuta el script `grover.py` usando el comando `python grover.py`.
