# importuje bibliotekę NumPy 
import numpy as np
# Pyta o dane wejściowe
a = float(input("Enter first value of square array: "))
b = float(input("Enter second value of square array : "))
c = float(input("Enter third value of square array : "))
d = float(input("Enter fourth value of square array : "))
# Tworzy szyk 2d 
m = np.array([[a, b], 
              [c, d]]) 
  
print("Printing the Original square array:\n", 
      m) 
  
# znajduje wartości własne i wektory własne 
w, v = np.linalg.eig(m) 
  
# drukuje własności własne 
print("Printing the Eigen values of the given square array:\n", 
      w) 
  
# drukuje wektory własne 
print("Printing Right eigenvectors of the given square array:\n",
      v)