import math

def solve():
    _, t = [int(n) for n in input().split()]
    smallest_cost = math.inf
    while True:
        try:
            line = input()
            cost_i, time_i = [int(n) for n in line.split()]
            if time_i <= t:
                if cost_i < smallest_cost:
                    smallest_cost = cost_i
        except EOFError:
            break
    
    print(smallest_cost if smallest_cost != math.inf else "TLE")


if __name__ == "__main__":
    solve()
