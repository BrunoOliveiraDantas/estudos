def sol():
    a,b = [ int(n) for n in input().split()] 
    return max(a+b, a-b, a*b)
    
if __name__== "__main__":
    print(sol())