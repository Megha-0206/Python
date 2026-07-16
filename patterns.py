#heart shape pattern with brute force
n=6
for i in range(n):
    for j in range(7):
        if ( i==0 and (j==1 or j==2 or j==4 or j==5)):
            print("* ",end="")
        elif(i==0 and (j==0 or j==3 or j==6)):
            print("  ",end="")
        elif(i==1 and (j==0 or j==3 or j==6)):
            print("* ",end="")
        elif(i==1 and (j==1 or j==2 or j==4 or j==5)):
            print("  ",end="")
        elif(i==2 and (j==0 or j==6 )):
            print("* ",end="")
        elif(i==2 and (j==1 or j==2 or j==3 or j==4 or j==5)):
            print("  ",end="")
        elif(i==3 and (j==1 or j==5)):
            print("* ",end="")
        elif(i==3 and (j==0 or j==2 or j==3 or j==4 or j==6)):
            print("  ",end="")
        elif(i==4 and (j==2 or j==4)):
            print("* ",end="")
        elif(i==4 and (j==0 or j==1 or j==3 or j==5 or j==6)):
            print("  ",end="")
        elif(i==5 and (j==3)):
            print("* ",end="")
        elif(i==5 and (j==0 or j==1 or j==2 or j==4 or j==5 or j==6)):
            print("  ",end="")
        else:
            print("  ",end="")
    print()
print("\n")
#Basic pattern 1:(Square Pattern)
n=5
for i in range(1,n):
    for j in range(1,n):
        print(j,end=" ")
    print("\r")
print("\n")
#Basic pattern 2:(Square 1 to 9 Number Pattern)
n=3
num=1
for i in range(0,n):
    for j in range(0,n):
        print(num,end=" ")
        num+=1
    print("\r")
print("\n")
#Basic pattern 3:(Square Character Pattern)
n=3
char ='A'
for i in range(0,n):
    for j in range(0,n):
        print(char,end=" ")
        char=chr(ord(char)+1)
    print("\r")
print("\n")
#Basic pattern 4:(Left Handed Triangle)
n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
print("\n")
#Basic pattern 5:(Inverted Right Handed Triangle)
n=5
for i in range(0,n):
    for j in range(0,i):
        print(" ",end = "")
    for j in range(0,n-i):
        print("*",end="")
    print("\r")
print("\n")
#Basic pattern 6:(Right Handed Triangle)
n=5
for i in range(0,5):
    for j in range(0,n-1-i):
        print("/",end="")
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
print("\n")
# Heart Shape Pattern
"""n=9
for i in range(0,n):
    for j in range(n):"""