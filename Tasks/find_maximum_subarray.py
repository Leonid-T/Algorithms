def find_maximum_subarray(A, low=0, high=None):
    if high is None:
        high = len(A)-1

    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = A[mid]-1
    summ = 0
    for i in range(mid, low-1, -1):
        summ += A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    right_sum = A[mid+1]-1
    summ = 0
    for i in range(mid+1, high+1):
        summ += A[i]
        if summ > right_sum:
            right_sum = summ
            max_right = i
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray2(A, low=0, high=None):
    if high is None:
        high = len(A)

    max_sum = A[0]-1
    summ = 0
    future_left = 0
    for i in range(high):
        summ += A[i]
        if summ > max_sum:
            max_sum = summ
            left = future_left
            right = i
        if summ < 0:
            summ = 0
            future_left = i + 1
    return left, right, max_sum


def main():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_maximum_subarray(A))
    print(find_maximum_subarray2(A))


if __name__ == '__main__':
    main()
