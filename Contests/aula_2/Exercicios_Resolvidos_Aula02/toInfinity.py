def solve(S, K):
    for c in S:
        if c != '1':
            return c

        K -= 1
        if K == 0:
            break

    return '1'

def main():
    S = input()
    K = int(input())
    
    result = solve(S, K)
    print(result)

if __name__ == "__main__":
    main()