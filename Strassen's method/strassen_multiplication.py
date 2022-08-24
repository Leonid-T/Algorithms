from math import log2

def strassen_multiplication(A, B):
    """
    Вступление к рекурсивному алгоритму произведения квадратных матриц A, B по
    методу Штрассена. Данный алгоритм выполняется для матриц с размерностью
    n = 2 ** x, для x >= 0
    """
    n = len(A)
    if n == len(A[0]) and n == len(B) and len(A[0]) == len(B[0]) and int(2**log2(n)) == n:
        return square_matrix_multiply(A, 0, n, 0, n,
                                      B, 0, n, 0, n)
    else:
        return None

def square_matrix_multiply(A, i_left_A, i_right_A, j_left_A, j_right_A,
                           B, i_left_B, i_right_B, j_left_B, j_right_B):
    """
    Реализация рекурсии к алгоритму Штрассена. Доступ к подматрицам основных
    матриц по начальным и конечным индексам основной матрицы.
    """
    n = i_right_A - i_left_A
    m = j_right_A - j_left_A
    C = [[0 for _ in range(m)] for _ in range(n)]
    if n == 1:
        C[0][0] = A[i_left_A][j_left_A] * B[i_left_B][j_left_B]
    else:
        i_mid_A = (i_left_A + i_right_A) // 2
        j_mid_A = (j_left_A + j_right_A) // 2
        i_mid_B = (i_left_B + i_right_B) // 2
        j_mid_B = (j_left_B + j_right_B) // 2
        S1 = matrix_operation(B, i_left_B,   i_mid_B,  j_mid_B, j_right_B,
                               B,  i_mid_B, i_right_B,  j_mid_B, j_right_B, '-')
        S2 =  matrix_operation(A, i_left_A,   i_mid_A, j_left_A,   j_mid_A,
                               A, i_left_A,   i_mid_A,  j_mid_A, j_right_A, '+')
        S3 =  matrix_operation(A,  i_mid_A, i_right_A, j_left_A,   j_mid_A,
                               A,  i_mid_A, i_right_A,  j_mid_A, j_right_A, '+')
        S4 =  matrix_operation(B,  i_mid_B, i_right_B, j_left_B,   j_mid_B,
                               B, i_left_B,   i_mid_B, j_left_B,   j_mid_B, '-')
        S5 =  matrix_operation(A, i_left_A,   i_mid_A, j_left_A,   j_mid_A,
                               A,  i_mid_A, i_right_A,  j_mid_A, j_right_A, '+')
        S6 =  matrix_operation(B, i_left_B,   i_mid_B, j_left_B,   j_mid_B,
                               B,  i_mid_B, i_right_B,  j_mid_B, j_right_B, '+')
        S7 =  matrix_operation(A, i_left_A,   i_mid_A,  j_mid_A, j_right_A,
                               A,  i_mid_A, i_right_A,  j_mid_A, j_right_A, '-')
        S8 =  matrix_operation(B,  i_mid_B, i_right_B, j_left_B,   j_mid_B,
                               B,  i_mid_B, i_right_B,  j_mid_B, j_right_B, '+')
        S9 =  matrix_operation(A, i_left_A,   i_mid_A, j_left_A,   j_mid_A,
                               A,  i_mid_A, i_right_A, j_left_A,   j_mid_A, '-')
        S10 = matrix_operation(B, i_left_B,   i_mid_B, j_left_B,   j_mid_B,
                               B, i_left_B,   i_mid_B,  j_mid_B, j_right_B, '+')
        P1 = square_matrix_multiply(A, i_left_A,   i_mid_A, j_left_A,   j_mid_A,
                                    S1,       0,   len(S1),        0,   len(S1))
        P2 = square_matrix_multiply(S2,       0,   len(S2),        0,   len(S2),
                                    B,  i_mid_B, i_right_B,  j_mid_B, j_right_B)
        P3 = square_matrix_multiply(S3,       0,   len(S3),        0,   len(S3),
                                    B, i_left_B,   i_mid_B, j_left_B,   j_mid_B)
        P4 = square_matrix_multiply(A,  i_mid_A, i_right_A,  j_mid_A, j_right_A,
                                    S4,       0,   len(S4),        0,   len(S4))
        P5 = square_matrix_multiply(S5,       0,   len(S5),        0,   len(S5),
                                    S6,       0,   len(S6),        0,   len(S6))
        P6 = square_matrix_multiply(S7,       0,   len(S7),        0,   len(S7),
                                    S8,       0,   len(S8),        0,   len(S8))
        P7 = square_matrix_multiply(S9,       0,   len(S9),        0,   len(S9),
                                    S10,      0,  len(S10),        0,  len(S10))
        i_mid_C = n // 2
        j_mid_C = m // 2
        for i in range(i_mid_C):
            for j in range(j_mid_C):
                C[i][j] = P5[i][j] + P4[i][j] - P2[i][j] + P6[i][j]
        for i in range(i_mid_C):
            for j in range(j_mid_C, m):
                C[i][j_mid_C] = P1[i][j-j_mid_C] + P2[i][j-j_mid_C]
        for i in range(i_mid_C, n):
            for j in range(j_mid_C):
                C[i][j] = P3[i-i_mid_C][j] + P4[i-i_mid_C][j]
        for i in range(i_mid_C, n):
            for j in range(j_mid_C, m):
                C[i][j] = P5[i-i_mid_C][j-j_mid_C] + P1[i-i_mid_C][j-j_mid_C] - P3[i-i_mid_C][j-j_mid_C] - P7[i-i_mid_C][j-j_mid_C]
    return C

def matrix_operation(A, i_left_A, i_right_A, j_left_A, j_right_A,
                     B, i_left_B, i_right_B, j_left_B, j_right_B, operator):
    if operator == '+':
        operator = lambda x, y: x + y
    elif operator == '-':
        operator = lambda x, y: x - y
    n = i_right_A - i_left_A
    return [[operator(A[i_left_A+i][j_left_A+j], B[i_left_B+i][j_left_B+j])
               for j in range(n)]
           for i in range(n)]

def ordinary_matrix_multiplication(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    A = [[1, 3],
         [7, 5]]
    B = [[6, 8],
         [5, 1]]
    # A = [[1, 3, 4],
    #      [7, 5, 9],
    #      [5, 0, 3]]
    # B = [[6, 8, 8],
    #      [5, 1, 0],
    #      [4, 2, 7]]
    C = strassen_multiplication(A, B)
    C1 = ordinary_matrix_multiplication(A, B)
    for row in C:
        print(row)
    print(C == C1)


if __name__ == '__main__':
    main()