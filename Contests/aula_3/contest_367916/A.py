def sol():
    a, b = [int(n) for n in input().split()]
    maximun = max(a,b)
    minimun = min(a,b)
    if maximun - minimun > 1 : return maximun + (maximun-1)
    return maximun + minimun

    
if __name__== "__main__":
    print(sol())