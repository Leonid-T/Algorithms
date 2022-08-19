def is_sum_of_two(x, A):
    A0 = A.copy()
    i = 0
    while i < len(A0):
        if A0[i] > x:
            A0.pop(i)
        else:
            i += 1
    if len(A0) == 0:
        return False

    middle = x // 2
    A1 = []
    A2 = []
    counter = 0
    for val in A0:
        if middle < val:
            A2.append(val)
        elif val < middle:
            A1.append(val)
        elif middle*2 == x:
            counter += 1
            if counter == 2:
                return True
        else:
            A1.append(val)    
    if len(A1) == 0 or len(A2) == 0:
        return False

    for i in range(len(A1)):
        A1[i] = x - A1[i]
    d = {}
    for val in A1:
        d[val] = True
    for val in A2:
        if d.get(val, False):
            return True
    return False

def main():
    A = [2, 4, 8, 4, 45, 23, 5, 7, 11, 10]
    x = 8
    print(is_sum_of_two(x, A))

if __name__ == '__main__':
    main()