import numpy as np

def calculate(input_list):
    # Verifica se a lista tem 9 elementos
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Transformar a lista em uma matriz 3x3
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calcular as estatísticas e gerar um dicionário em que cada chave corresponde a uma estatística (média, variância, etc.)
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.flatten().mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.flatten().var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.flatten().std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.flatten().max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.flatten().min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.flatten().sum()]
    }

    return calculations
