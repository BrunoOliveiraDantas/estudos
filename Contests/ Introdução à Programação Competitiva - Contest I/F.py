def digit_sum(num):
    return sum(map(int, str(num)))

def min_digit_sum(n):
    min_sum = float('inf')
    for i in range(1, n):
        a = i
        b = n - i
        digit_sum_a = digit_sum(a)
        digit_sum_b = digit_sum(b)
        min_sum = min(min_sum, digit_sum_a + digit_sum_b)
    return min_sum


if __name__== "__main__":
    n = int(input())
    print(min_digit_sum(n))