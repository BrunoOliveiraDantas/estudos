def sol():
    a = [int(n) for n in input().split()] 
    k = int(input())
    for j in range(0, k): 
        index = a.index(max(a))
        a[index]= max(a)*2  

    return sum(a)
    
if __name__== "__main__":
    print(sol())