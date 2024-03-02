import sys

def sol():
    numbers = [ int(n) for n in sys.stdin.readlines()][:-1]
    for n in numbers:
        if n%17 == 0:
            print("1")
        else:
            print("0")
        
if __name__== "__main__":
    sol()