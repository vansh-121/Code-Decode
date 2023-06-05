# Code - Decode Setup:
print("Welcome sir, what do you want us to do?")
print("Press 1: Code\nPress 2: Decode ")
A = int(input("Enter your no.here: "))
a = input("Enter your secret message: ")
def move():
    if(A == 1):
        pass
        if( len(a) <= 3  ):
            c = a[1:] + a[0]
            print(c)
        else:    
            c = a[1:] + a[0]
            d = "%$#" + c + "^@!"
            print(d)
def rev():
    if(A == 2):
        if( len(a) <= 3  ):
            c = a[-1] + a[0:-1] 
            print(c)
        else:
            if (a.isalpha()):
                c = a[-1] + a[0:-1]
                print(c)
            else:
                c = a[3:-3]
                D = c[-1] + c[0:-1]
                print(D)
move()
rev()



