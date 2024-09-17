UserInt1 = int(0)
UserInt2 = int(0)
UserOpp = "+"

Answer = int(0)
ValidOpp = ["+","-","/","x"]
IntroText = "This is a basic calculator that can Add(+), Subtract(-), Divide(/) and Multiply(x)"
x=0


while (x==0):
    print(IntroText)
    UserOpp = input("what type of opperation would you like to do\n")
    if UserOpp == ValidOpp [0]:
        UserInt1 = int(input("Enter the first Number\n"))
        UserInt2 = int(input("Enter the Seccound Number\n"))
        Answer = UserInt1 + UserInt1
        print ("The Awnser to ", UserInt1, " ", UserOpp, " ",UserInt2, " Is ",Answer)
        input

    elif UserOpp == ValidOpp [1]:
        UserInt1 = int(input("Enter the first Number\n"))
        UserInt2 = int(input("Enter the Seccound Number\n"))
        Answer = UserInt1 - UserInt1
        print ("The Awnser to ", UserInt1, " ", UserOpp, " ",UserInt2, " Is ",Answer)
        input
    
    elif UserOpp == ValidOpp [2]:
        UserInt1 = int(input("Enter the first Number\n"))
        UserInt2 = int(input("Enter the Seccound Number\n"))
        Answer = UserInt1 / UserInt1
        print ("The Awnser to ", UserInt1, " ", UserOpp, " ",UserInt2, " Is ",Answer)
        input

    elif UserOpp == ValidOpp [3]:
        UserInt1 = int(input("Enter the first Number\n"))
        UserInt2 = int(input("Enter the Seccound Number\n"))
        Answer = UserInt1 * UserInt1
        print ("The Awnser to ", UserInt1, " ", UserOpp, " ",UserInt2, " Is ",Answer)
        input
    
    else:  
        print(UserOpp, "is an Unsupported Opperation\n Please Use of of these 4 opporations ",ValidOpp)