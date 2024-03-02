def solve():
    n = int(input())
    number_of_pairs = int(n / 2)
    odds = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            odds += 1
    print(number_of_pairs * odds)


if __name__ == "__main__":
    solve()
