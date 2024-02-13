def sol():
    a,b,x = [ int(n) for n in input().split()] 
    if x <= a + b and x >= a:
        return "YES"
    else:
        return "NO"
    
if __name__== "__main__":
    print(sol())