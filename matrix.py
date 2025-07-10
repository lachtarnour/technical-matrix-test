class Matrix(object):
    """
    Classe pour représenter une matrice et réaliser les opérations de base :
    addition, soustraction, multiplication et calcul du déterminant.
    """

    def __init__(self, mat):
        if self.verify_matrix(mat):
            self.mat = [row[:] for row in mat]  # copie profonde simple
        else:
            raise ValueError("Format de matrice invalide")

    def verify_matrix(self, mat):
        if type(mat[0]) in (float, int):
            return True
        row_size = [len(i) for i in mat]
        return len(set(row_size)) == 1

    def matrix_shape(self, mat):
        if type(mat[0]) in (float, int):
            return (len(mat), 0)
        else:
            return (len(mat), len(mat[0]))

    def __add__(self, mat2):
        return Matrix(self.add(mat2))

    def __sub__(self, mat2):
        return Matrix(self.soustract(mat2))

    def __mul__(self, mat2):
        return Matrix(self.mult(mat2))

    def add(self, mat2):
        mat2 = mat2.mat
        shape_1 = self.matrix_shape(self.mat)
        shape_2 = self.matrix_shape(mat2)
        if shape_1 != shape_2:
            raise ValueError("Dimensions incompatibles pour l'addition")
        return [[self.mat[i][j] + mat2[i][j] for j in range(shape_1[1])]
                for i in range(shape_1[0])]

    def soustract(self, mat2):
        mat2 = mat2.mat
        shape_1 = self.matrix_shape(self.mat)
        shape_2 = self.matrix_shape(mat2)
        if shape_1 != shape_2:
            raise ValueError("Dimensions incompatibles pour la soustraction")
        return [[self.mat[i][j] - mat2[i][j] for j in range(shape_1[1])]
                for i in range(shape_1[0])]

    def mult(self, mat2):
        mat2 = mat2.mat
        shape_1 = self.matrix_shape(self.mat)
        shape_2 = self.matrix_shape(mat2)
        if shape_1[1] != shape_2[0]:
            raise ValueError("Dimensions incompatibles pour la multiplication")

        result = [[0 for _ in range(shape_2[1])] for _ in range(shape_1[0])]
        for i in range(shape_1[0]):
            for j in range(shape_2[1]):
                for k in range(shape_1[1]):
                    result[i][j] += self.mat[i][k] * mat2[k][j]
        return result

    def get_minor(self, A, row, col):
        return [  # copie de A sans ligne i et colonne j
            [A[i][j] for j in range(len(A)) if j != col]
            for i in range(len(A)) if i != row
        ]

    def determinant(self):
        return self._det(self.mat)

    def _det(self, A):
        n = len(A)
        if n == 1:
            return A[0][0]
        if n == 2:
            return A[0][0]*A[1][1] - A[0][1]*A[1][0]

        det = 0
        for j in range(n):
            cofactor = (-1) ** j * A[0][j] * self._det(self.get_minor(A, 0, j))
            det += cofactor
        return det