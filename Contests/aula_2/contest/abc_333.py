def solve():
    a, b = [int(digit) for digit in input().split()]
    ans = "No"
    for i in range(1, 3):
        if (a * b * i) % 2 != 0:
            ans = "Yes"
        break

    print(ans)

if __name__ == "__main__":
    solve()