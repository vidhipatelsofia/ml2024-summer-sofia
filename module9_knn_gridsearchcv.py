import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def main():

    N = int(input("Enter the number of training data points (N): "))
    print(f"Enter {N} (x, y) pairs for the training set:")
    
    train_x = []
    train_y = []
    for i in range(N):
        x = float(input(f"Enter x value for pair {i + 1}: "))
        y = int(input(f"Enter y value for pair {i + 1}: "))
        train_x.append(x)
        train_y.append(y)
    
    train_x = np.array(train_x).reshape(-1, 1)
    train_y = np.array(train_y)
    
    M = int(input("Enter the number of test data points (M): "))
    print(f"Enter {M} (x, y) pairs for the test set:")
    
    test_x = []
    test_y = []
    for i in range(M):
        x = float(input(f"Enter x value for pair {i + 1}: "))
        y = int(input(f"Enter y value for pair {i + 1}: "))
        test_x.append(x)
        test_y.append(y)
    
    test_x = np.array(test_x).reshape(-1, 1)
    test_y = np.array(test_y)
    
    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': range(1, 11)}  # k values from 1 to 10
    
    grid_search = GridSearchCV(knn, param_grid, scoring='accuracy', cv=5)
    grid_search.fit(train_x, train_y)
    
    best_k = grid_search.best_params_['n_neighbors']
    best_knn = grid_search.best_estimator_
    
    test_predictions = best_knn.predict(test_x)
    test_accuracy = accuracy_score(test_y, test_predictions)
    
    print(f"The best k value is: {best_k}")
    print(f"The test accuracy with k={best_k} is: {test_accuracy:.2f}")

if __name__ == "__main__":
    main()

