def strassen_multiplication(A, B):
    """
    Вступление к рекурсивному алгоритму произведения квадратных матриц A, B по
    методу Штрассена.
    """
    if len(A) == len(A[0]) and len(A) == len(B) and len(A[0]) == len(B[0]):
        n = len(A)
        C = [[0 for _ in range(n)] for _ in range(n)] #выделение памяти под C
        return square_matrix_multiply(A, 0, n, 0, n,
                                      B, 0, n, 0, n, C)
    else:
        return None

def square_matrix_multiply(A, i_left_A, i_right_A, j_left_A, j_right_A,
                           B, i_left_B, i_right_B, j_left_B, j_right_B, C):
    """
    Реализация рекурсии к алгоритму Штрассена. Доступ к подматрицам основных
    матриц по начальным и конечным индексам основной матрицы.
    """
    if i_left_A == i_right_A:
        C[i_left_A][j_left_A] = A[i_left_A][j_left_A] * B[i_left_B][j_left_B]
    else:
        i_mid_A = i_right_A - i_right_A
        j_mid_A = j_right_A - j_right_A
        i_mid_B = i_right_B - i_right_B
        j_mid_B = j_right_B - j_right_B
        S1 = matrix_operation(B, i_left_B, i_right_B,  j_mid_B, j_right_B,
                              B,  i_mid_B, i_right_B,  j_mid_B, j_right_B, '-')
        S2 = matrix_operation(A, i_left_A,   i_mid_A, j_left_A,   j_mid_A,
                              A, i_left_A,   i_mid_A,  j_mid_A, j_right_A, '-')
        """
        Создать оставшиеся матрицы Si: 3 <= i <= 10.
        Запустить рекурсию по подматрицам Pi: 1 <= i <= 7.
        Собрать исходную матрицу C по матрицам Pi.
        """

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

def main():
    A = [[85, 25, 43, 75],
         [34, 84, 24, 15],
         [32, 37, 89, 15],
         [18, 37, 54, 87]]
    B = [[27, 72, 17, 38],
         [57, 37, 21, 46],
         [38, 27, 84, 28],
         [29, 68, 25, 65]]
    C = strassen_multiplication(A, B)
    for row in C:
        print(row)

if __name__ == '__main__':
    main()