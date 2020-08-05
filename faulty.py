l=['*','-','/','+','n']
while True:
    oprtr=input('\n\nEnter what do you want to do \npress + for addition\npress / for division\npress - for subtraction\npress * for multiplication\npress n for exit\n')
    if oprtr in l:
        if oprtr=='n':
            break
        else:
            a=eval(input('enter first no.'))
            b=eval(input("enter second no."))
            if a==65 and b==67 and oprtr=='*':
                print(58765)
            elif a==89 and b==77 and oprtr=='+':
                print(147)
            elif a==435 and b==13 and oprtr=='/':
                print(19.45)
            elif oprtr=='+':
                print(a+b)
            elif oprtr=='*':
                print(a*b)
            elif oprtr=='-':
                print(a-b)
            elif oprtr=='/':
                print(a/b)
    else:
        print('Error:InvalidInput')
