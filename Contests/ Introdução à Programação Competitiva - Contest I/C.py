def sol():
    a,b = [ int(n) for n in input().split()] 
    return "Yay!" if a + b <= 16 and (a <= 8 and b <= 8) else ":("  
    
if __name__== "__main__":
    print(sol())