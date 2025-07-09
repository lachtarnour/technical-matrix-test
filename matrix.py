
class Matrix(object):
    """
    Classe pour représenter une matrice et réaliser les opérations de base :
    addition, soustraction, multiplication et calcul du déterminant.
    """
    
    
    # 1. initialize a matrix: ex.mat = Matrix([[1,2,3],[1,2,3]])

    # 2. realize the basic operation add: ex. mat1 + mat2 = mat3

    # 3. calculate the determinant of a matrix: ex. mat.det


    #Implémenter les opérations de base sur des matrices : addition, soustraction, multiplication.


    def __init__(self,mat):
        if self.verify_matrix(mat):
            self.mat = mat
        else:
            pass
        

    def verify_matrix(self,mat):
        if type(mat[0]) == float or type(mat[0]) == int:
            return(True)
        row_size = [len(i) for i in mat]
        if len(set(row_size))==1:
            print("good format")
            return(True)
        else: 
            print("bad format")
            return(False)
        
    def matrix_shape(self,mat):
        if type(mat[0]) == float or type(mat[0]) == int:
            return(len(mat),0)
        else:
            return(len(mat),len(mat[0]))
    

    def add(self,mat2):
        shape_1 = self.matrix_shape(self.mat)
        mat2 = mat2.mat
        shape_2 = self.matrix_shape(mat2)
        if not(shape_1[0]== shape_2[0] and shape_1[1]== shape_2[1]):
            return None
        
        result = self.mat.copy()

        for i in range(shape_1[0]):
            for j in range(shape_1[1]):
                result[i][j] = self.mat[i][j] + mat2[i][j]

        return result
    
    def soustract(self,mat2):
        shape_1 = self.matrix_shape(self.mat)
        mat2 = mat2.mat
        shape_2 = self.matrix_shape(mat2)
        if not(shape_1[0]== shape_2[0] and shape_1[1]== shape_2[1]):
            return None
        
        result = self.mat.copy()

        for i in range(shape_1[0]):
            for j in range(shape_1[1]):
                result[i][j] = self.mat[i][j] - mat2[i][j]

        return result
    

    def mult(self,mat2):
        ## erreur
        shape_1 = self.matrix_shape(self.mat)
        mat2 = mat2.mat
        shape_2 = self.matrix_shape(mat2)

        # verify shape 
        if not((shape_1[0] == shape_1[1]) and  (shape_2[0] == shape_2[1]) and (shape_1[0] == shape_2[0])):
            return None
        n = shape_1[0]
        result = self.mat.copy()

        for i in range(n):
            for j in range(n):
                s = 0
                for k in range(n):
                    s+= self.mat[i][k] * mat2[k][j]
                result[i][j] = s
        return result

    def del_ligne(self,A,i):
        A.pop(i)
        return A

    def del_column(self,A,j):
        A_copy = A.copy()
        if j == 0:
            A_copy = [row[1:] for row in A_copy]
        else:
            A_copy = [row[:j-1] + row[j+1:] for row in A_copy]
        return A_copy


    def det(self,A):
        det = 0
        i = 0
        j = 0
        A_ij = self.del_ligne(A,i)
        A_ij = self.del_column(A,j)
        if len(A_ij) == 1 and len(A_ij[0]) == 1:
            det += (-1)**(i+j) * A_ij[0][0]
            j = j + 1
        else:
            det += (-1)**(i+j) * det(A_ij)


        



if __name__ == '__main__':
    # Example

    # Test for #1
    # mat1 = Matrix([[1,2,3],[1,4,3],[1,4,4]])

    # Test for #2
    # mat2 = Matrix([[1,2,3],[1,4,3],[1,4,4]])
    # mat3 = mat1 + mat2

    # Test for #3
    # print(mat1.det())
    # print(mat3)
    pass
