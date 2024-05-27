import numpy as np

# Genera la matriz de Hadamard
def hadamard_matrix():
    return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Calcula el producto tensorial
def kronecker_product(A, B):
    return np.kron(A, B)

# Genera una matriz identidad de tamaño n
def identity_matrix(size):
    return np.eye(size)

# Crea el operador de difusión
def create_diffusion_operator(size):
    uniform_state = np.ones((2**size, 2**size)) / (2**size)
    return 2 * uniform_state - identity_matrix(2**size)

# Construye el oráculo
def build_oracle(size, target_index):
    oracle_matrix = identity_matrix(2**size)
    oracle_matrix[target_index, target_index] = -1
    return oracle_matrix

# Implementa el algoritmo de Grover
def grover_search_algorithm(size, oracle):
    initial_state = np.zeros((2**size, 1))
    initial_state[0] = 1
    
    H = hadamard_matrix()
    full_hadamard = H
    for _ in range(size-1):
        full_hadamard = kronecker_product(full_hadamard, H)
    
    current_state = np.dot(full_hadamard, initial_state)
    
    iteration_count = int(np.pi / 4 * np.sqrt(2**size))
    
    for _ in range(iteration_count):
        current_state = np.dot(oracle, current_state)
        D = create_diffusion_operator(size)
        current_state = np.dot(D, current_state)
    
    return current_state

# Busca un número en un array utilizando Grover
def find_number(arr, target):
    size = int(np.ceil(np.log2(len(arr))))
    padded_size = 2**size
    extended_arr = np.pad(arr, (0, padded_size - len(arr)), mode='constant')
    
    target_index = np.where(extended_arr == target)[0][0]
    
    oracle = build_oracle(size, target_index)
    
    final_state = grover_search_algorithm(size, oracle)
    
    probability_distribution = np.abs(final_state)**2
    
    for i in range(len(probability_distribution)):
        print(f"State |{i:0{size}b}>: Probability = {probability_distribution[i][0]:.4f}")
    
    return np.argmax(probability_distribution)

# Ejemplo de uso
array_example = np.random.permutation(16)  # Array desordenado de 16 números
search_target = 4

print(f"Array: {array_example}")
print(f"Buscando el número {search_target} en el array.")

found_index = find_number(array_example, search_target)
print(f"El número {search_target} se encontró en la posición {found_index+1} del array.")
