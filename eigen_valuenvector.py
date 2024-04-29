# importing numpy library 
import numpy as np
# asking for inputs
a = float(input("Enter first value of square array: "))
b = float(input("Enter second value of square array : "))
c = float(input("Enter third value of square array : "))
d = float(input("Enter fourth value of square array : "))
# create numpy 2d-array 
m = np.array([[a, b], 
              [c, d]]) 
  
print("Printing the Original square array:\n", 
      m) 
  
# finding eigenvalues and eigenvectors 
w, v = np.linalg.eig(m) 
  
# printing eigen values 
print("Printing the Eigen values of the given square array:\n", 
      w) 
  
# printing eigen vectors 
print("Printing Right eigenvectors of the given square array:\n",
      v)