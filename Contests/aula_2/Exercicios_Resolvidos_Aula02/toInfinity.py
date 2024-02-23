def sol():
    s = input()
    k = int(input())    
    
    for  digit in s:
        if digit != "1":
            print(digit)
            break
        if k == 1:
            print("1")
            break
        k -= 1
        continue

    
if __name__== "__main__":
    sol()