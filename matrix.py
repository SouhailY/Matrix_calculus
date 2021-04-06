import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        determinant=0
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        elif self.h==2:
            determinant=self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
        else:
            determinant=1.0/self.g[0][0]
        
        return determinant
            

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        trace=0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        for i in range (self.h):
            trace = trace + self.g[i][i]
            
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        row=[]
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        elif self.h==1:
            row.append(1.0/self.g[0][0])
            inverse.append(row)
        else:
            determinant=self.determinant()
            trace=self.trace()
            Id=identity(2)
            
            for i in range (self.h):
                for j in range (self.w):
                    row.append((1.0/determinant)*(trace*Id[i][j]-self.g[i][j]))
                inverse.append(row)
                row=[]
        return Matrix(inverse)
                                         

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        transpose=[]
        row=[]
        for i in range (self.w):
            for j in range (self.h):
                row.append(self.g[j][i])
            transpose.append(row)
            row=[]
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        addition = []
        row=[]
        for i in range (self.h):
            for j in range (self.w):
                row.append(self.g[i][j]+other.g[i][j])
            addition.append(row)
            row=[]
        
        return Matrix(addition)
                         
                

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        negative = []
        row=[]
        for i in range (self.h):
            for j in range (self.w):
                row.append(-self.g[i][j])
            negative.append(row)
            row=[]  
              
        return Matrix(negative)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        subtraction = []
        row=[]
        for i in range (self.h):
            for j in range (self.w):
                row.append(self.g[i][j]-other.g[i][j])
            subtraction.append(row)
            row=[]
        
        return Matrix(subtraction)


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        product = []
        row=[]
        
        for i in range (self.h):
            for j in range (other.w):
                a=0
                for k in range (other.h):
                    a=a+(self.g[i][k]*other.g[k][j])
                row.append(a)
            product.append(row)
            row=[]
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        product = []
        row=[]
        if isinstance(other, numbers.Number):
            pass
            for i in range (self.h):
                for j in range (self.w):
                    row.append(other*self.g[i][j])
                product.append(row)
                row=[]
        return Matrix(product)
                    
            