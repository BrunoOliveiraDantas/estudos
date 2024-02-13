def digit_sum(num):
    return sum(map(int, str(num)))

def min_digit_sum(n):
    min_sum = float('inf')
    for i in range(1, n):
        a = i
        b = n - i
        digit_sum_a = d