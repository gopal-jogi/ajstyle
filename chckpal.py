def check_pallindrome(num):
    pal = 0
    while num:
        rem = num %10
        pal = pal *10 +rem
        num //= 10
    return pal

def read_input(called_function):
    n = int(input("Enter a number : "))
    res = called_function(n)
    if res == n:
        print("The number is a pallindrome")
    else:
        print("The number is not a pallindrome")
    

read_input(check_pallindrome)

#Output
#C:\Users\FY\AppData\Local\Programs\Python\Python310>chckpal.py
#Enter a number : 12321
#The number is a pallindrome
