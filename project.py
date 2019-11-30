k = 1
print("*******************************************\n"
      "*****************MATHS GAME****************\n"
      "*******************************************\n")
print( "**INSTRUCTIONS TO PLAY\n"
       " enter 1 for factorial\n"
       " enter 2 to check whether it is palindrome or not\n"
       " enter 3 to find factors of a number\n"
       " enter 4 to find nth fibonnaci series\n"
       " enter 5 to  exit  ")
while (k > 0):
    choice=int(input("enter your operation: "))
    if choice==1:
        number=int(input("enter the number: "))
        a=number
        s=1
        while a>0:
            s=s*a
            a-=1
        print(f"the factorial of {number} is {s}")
        k+=1

    elif choice==2:
        number = str(input("enter the number: "))
        reverse= number[::-1]
        if reverse==number:
            print(f"the number {number} is a palindrome")
        else:
            print(f"the number {number} is not a palindrome")
        k+=1
    elif choice==3:
        number = int(input("enter the number: "))
        print(f"the factors of {number} are : ")
        for i in range (1,number):
            if(number%i==0):
                print(i)
        k+=1

    elif choice==4:
        number = int(input("enter the number: "))
        a=0
        b=1
        c=0
        print(f"the fibonacci series of a {number} is: ")
        while (c <=number):
            print(f"{c} ")
            c=a+b
            a=b
            b=c
            k+=1

    elif choice==5:
        assure=str(input("are u sure u what to quit :"))
        if(assure.upper()=='YES'):
            print("thank you for playing")
            print("EXIT")
            k=0
        elif(assure.lower()=='NO'):
            k=1

    else:
        print("wrong key pressed")
        k+=1
