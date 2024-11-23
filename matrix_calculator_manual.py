# python 3.12.3 64-bit

"""
Task 1: Matrix Calculator with NumPy
This will be a simple project that introduces you to NumPy, a core library used 
in AI and data science for efficient matrix and array operations.

What You'll Build:
A program that can perform basic matrix operations:
Addition
Subtraction
Multiplication
Why This is Great:
It's a small, manageable task.
You'll get comfortable with NumPy, which is fundamental in machine learning and 
deep learning.
You'll feel the reward of completing a project quickly, helping you build 
momentum.
Steps:
Create two matrices.
Implement functions to perform addition, subtraction, and multiplication of 
these matrices.
Print the results.
"""

import re

"""Error block."""
class NotAMatrixError(Exception):
    """Raised when the user inputs an object that has unequal rows or columns."""
    pass
class MismatchingMatricesError(Exception):
    """Raised when the user tries to make 2 unsuitable matrices interact (e.g.,
    unequal rows or columns in 2 matrices used for addition, or unequal columns
    of matrix 1 and rows of matrix 2 used for multiplication)."""
    pass
class NonExistingMatrixError(Exception):
    """Raised when the user tries to execute an operation on matrix that was not 
    inputted."""
    pass
class UnsuitableMatrixError(Exception):
    """Raised when a matrix does not satisfy conditions of the operation."""


def get_matrix():
    """Gets a matrix from user input. Returns the matrix."""
    # Initiate a matrix (a list (rows) of lists (column values)).
    M = []
    # Ask the user for the number of rows and columns.
    num_rows = int(input(f"How many rows is in the matrix?\n"))
    num_cols = int(input(f"How many columns is in the matrix?\n"))

    for i in range(num_rows): # For every row in the matrix.
        # Get the values in the row.
        row_str = input(f"Enter the row of the matrix: ")
        # Turn them into separate elements of a list (str).
        row_str = re.split(r"[\s,|+\-!]+", row_str)
        # Check if it is truly a matrix (if every row is equal in length).
        if len(row_str) != num_cols:
            raise NotAMatrixError(f"The number of numbers in each row must be {num_cols}.")
        # Turn every separate str into an int object.
        row_int = [int(j) for j in row_str]

        # Add this row to the matrix.
        M.append(row_int)
    # Output the resulting matrix.
    return M


class Manual_Matrix_Calculator:
    """
    Takes in 1 or 2 matrices and performs manual calculations like addition,
    subtraction, multiplication, transposing, inverting and finding determinant.
    """
    def __init__(self, matrix1, matrix2=None):
        # Check that matrices exist and that the inputted objects are truly 
        # matrices.
        self.A = matrix1
        if not self.A:
            raise NonExistingMatrixError("Matrix 1 was not given.")
        if len(self.A) == 1 or len(self.A[0]) == 1:
            raise NotAMatrixError(
                "Object 1 is a vector, not a matrix")
        for i in range(len(self.A)-1):
            if len(self.A[i]) != len(self.A[i+1]):
                raise NotAMatrixError(
                    "Object 1 is not a matrix. Wrong dimensions.")
            
        self.B = matrix2
        if self.B:
            if len(self.B) == 1 or len(self.B[0]) == 1:
                raise NotAMatrixError(
                "Object 2 is a vector, not a matrix")
            for i in range(len(self.B)-1):
                if len(self.B[i]) != len(self.B[i+1]):
                    raise NotAMatrixError(
                        "Object 2 is not a matrix. Wrong dimensions.")

    def add(self):
        """Adds 2 matrices between each other. Returns the result."""
        # Check if matrix 2 exists
        if not self.B:
            raise NonExistingMatrixError("Matrix 2 was not given.")

        # Initialize the result matrix with the correct dimensions.
        C = [[0 for _ in range(len(self.A[0]))] for _ in range(len(self.A))]

        # Check for equal number of rows.
        if len(self.A) != len(self.B):
            raise MismatchingMatricesError(
                "The number of rows must be equal in 2 matrices.")
        
        for i in range(len(self.A)): # for every row
            # Check for equal number of columns.
            if len(self.A[i]) != len(self.B[i]):
                raise MismatchingMatricesError(
                    "The number of columns must be equal in 2 matrices.")

            for j in range(len(self.A[i])): # for every col value in this row
                # Add an element in matrix B to a corresponding element in 
                # matrix A.
                C[i][j] = self.A[i][j] + self.B[i][j]
        
        # Return the result.
        return C
    
    def subtract(self):
        """Subtracts one matrix from the other. Returns the result."""
        # Check if matrix 2 exists
        if not self.B:
            raise NonExistingMatrixError("Matrix 2 was not given.")

        # Initialize the result matrix with the correct dimensions.
        C = [[0 for _ in range(len(self.A[0]))] for _ in range(len(self.A))]
        
        # Check for equal number of rows.
        if len(self.A) != len(self.B):
            raise MismatchingMatricesError(
                "The number of rows must be equal in 2 matrices.")
        
        for i in range(len(self.A)): # for every row
            # Check for equal number of columns.
            if len(self.A[i]) != len(self.B[i]):
                raise MismatchingMatricesError(
                    "The number of columns must be equal in 2 matrices.")

            for j in range(len(self.A[i])): # for every col value in this row
                # Subtract an element in matrix B from a corresponding element 
                # in matrix A.
                C[i][j] = self.A[i][j] - self.B[i][j]
        
        # Return the result.
        return C
    
    def multiplicate(self):
        """Multiplies one matrix by the other. Returns the multiplied result."""
        # Check if matrix 2 exists
        if not self.B:
            raise NonExistingMatrixError("Matrix 2 was not given.")

        # Initialize the result matrix with the correct dimensions.
        C = [[0 for _ in range(len(self.B[0]))] for _ in range(len(self.A))]

        # Check if the matrices satisfy the reqs for matrix multiplication.
        if len(self.A[0]) != len(self.B):
            raise MismatchingMatricesError(
                "The number of columns in matrix 1 must be equal to the number of rows in matrix 2.")
        
        # Multiply.
        for i in range(len(self.A)): # Iterate over each row of A.
            for j in range(len(self.B[0])): # Over each column of B.
                for k in range(len(self.B)): # Over each element in col of B (or in row of A).
                    C[i][j] += self.A[i][k] * self.B[k][j]
        
        # Return the result.
        return C
    
    def transpose(self):
        """Returns the transpose of the matrix 1."""
        # Initialize the result matrix with the correct dimensions.
        C = [[0 for _ in range(len(self.A))] for _ in range(len(self.A[0]))]

        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                C[j][i] = self.A[i][j]
        
        # Return the result.
        return C
    
    def calculate_determinant(self):
        """Returns the determinant of the matrix 1."""
        # Check if the matrix is suitable for the operation.
        # Check if it's square.
        if len(self.A) != len(self.A[0]):
            raise UnsuitableMatrixError("The matrix must be square to have a determinant.")
        # Check if it's not bigger than 3x3 (program limitation).
        if len(self.A) > 3:
            print("Sorry, max size of the matrix that the method can handle is 3x3.")
            return

        # Calculate the determinant.
        # 2x2.
        elif len(self.A) == 2:
            determinant = (self.A[0][0] * self.A[1][1]) - (self.A [0][1] * self.A[1][0])
            
            # Return the result.
            return determinant

        # 3x3.
        else: # if len(self.A) == 3
            arg1 = (self.A[1][1] * self.A[2][2]) - (self.A [1][2] * self.A[2][1])
            arg2 = (self.A[1][0] * self.A[2][2]) - (self.A [1][2] * self.A[2][0])
            arg3 = (self.A[1][0] * self.A[2][1]) - (self.A [1][1] * self.A[2][0])
            determinant = 0
            determinant += self.A[0][0] * arg1
            determinant -= self.A[0][1] * arg2
            determinant += self.A[0][2] * arg3

            # Return the result.
            return determinant
        
    def invert(self):
        # Check if the matrix is suitable for the operation.
        # Check if the determinant is non-zero (+ all the checks included in 
        # the calculate_determinant method):
        if self.calculate_determinant() == 0:
            print("The determinant of the matrix must be non-zero.")
            return
        # Check if the matrix is not bigger than 2x2 (program limitation).
        if len(self.A) > 2:
            print("Sorry, max size of the matrix that the method can handle is 3x3.")
            return
        
        # Initialize an object to store the inverse matrix.
        A_inv = [[], []]

        # Calculate the inverse.
        adminusbc = self.A[0][0] * self.A[1][1] - self.A[0][1] * self.A[1][0]
        A_inv[0][0] = self.A[1][1] / adminusbc
        A_inv[0][1] = -self.A[0][1] / adminusbc
        A_inv[1][0] = -self.A[1][0] / adminusbc
        A_inv[1][1] = -self.A[0][0] / adminusbc

        # Return the result.
        return A_inv


"""Test block."""
def main():
    # Test get_matrix function.
    A = get_matrix()
    print(A)

    # Test the manual matrix calculator methods.
    # Test manual addition.
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8, 9], [10, 11, 12]]
    manual_calc = Manual_Matrix_Calculator(A, B)
    C = manual_calc.add()
    print(C)

    # Test manual subtraction.
    C = manual_calc.subtract()
    print(C)

    # Test manual multiplication.
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    manual_calc = Manual_Matrix_Calculator(A, B)
    C = manual_calc.multiplicate()
    print(C)

    # Test manual transpose.
    A = [[1, 2, 3], [4, 5, 6]]
    manual_calc = Manual_Matrix_Calculator(A)
    C = manual_calc.transpose()
    print(C)

    # Test manual determinant.
    # 2x2.
    A = [[1, 2], [3, 4]]
    manual_calc = Manual_Matrix_Calculator(A)
    determinant_A = manual_calc.calculate_determinant()
    print(determinant_A)
    # 3x3.
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    manual_calc = Manual_Matrix_Calculator(A)
    determinant_A = manual_calc.calculate_determinant()
    print(determinant_A)

    # Test manual inverting.
    A = [[1, 2], [3, 4]]
    manual_calc = Manual_Matrix_Calculator(A)
    inverse_A = manual_calc.invert()
    print(inverse_A)
    # Check if it's truly inverse:
    I = [[1, 0], [0, 1]]
    manual_calc = Manual_Matrix_Calculator(A, inverse_A)
    print(manual_calc.multiplicate() == I)

# Run the tests.
if __name__ == "__main__":
    main()

