def sol():
    a,b,x = [ int(n) for n in input().split()] 
    if a >= x:
        return "NO"
    elif a+b <= x:
        return "NO"
    elif x < a:
        return "NO"
    return "YES"

    
if __name__== "__main__":
    print(sol())