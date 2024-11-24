import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_values():
    while True:
        try:
            N = int(input("Please enter the number of (x, y) points (N): "))
            if N <= 0:
                raise ValueError("N must be a positive integer.")
            break
        except ValueError as e:
            print(e)
    
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)
    
    print(f"Please enter {N} (x, y) pairs:")
    for i in range(N):
        while True:
            try:
                x = int(input(f"Enter x (ground truth) for point {i+1} (0 or 1): "))
                y = int(input(f"Enter y (predicted class) for point {i+1} (0 or 1): "))
                if x not in [0, 1] or y not in [0, 1]:
                    raise ValueError("Both x and y must be 0 or 1.")
                X[i] = x
                Y[i] = y
                break
            except ValueError as e:
                print(e)
    
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    
    print("\nResults:")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")