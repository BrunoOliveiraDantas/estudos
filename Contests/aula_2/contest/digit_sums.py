import sys

def solve():
    n, t = [int(n) for i in sys.stdin.readline().split()]
    
    a = input()
    divider = 0
    for char in a:
        divider += int(char)

    ans = "Yes" if int(a) % divider == 0 else "No"
    print(ans)

if __name__ == "__main__":
    solve()