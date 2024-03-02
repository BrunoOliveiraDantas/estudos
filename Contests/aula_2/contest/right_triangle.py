def solve():
    a, b, c = [int(digit) for digit in input().split()]
    area = int(b * a / 2)
    print(area)

if __name__ == "__main__":
    solve()