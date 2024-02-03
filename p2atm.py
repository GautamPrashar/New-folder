# while True:
#     print("Enter ur choice")
#     print("Enter 1 for addition")
#     print("Enter 2 for subtraction")
#     print("Enter 3 for multiplication")
#     print("Enter 4 for divsion")
#     choice=int(input("Enter your choice"))
#     x=int(input("Enter number:"))
#     y=int(input("Enter number:"))
#     if choice==1:
#         print(x+y)
#     elif choice==2:
#         print(x-y)
#     elif choice==3:
#         print(x*y)
#     elif choice==4:
#         print(x/y)
#     else:
#         print("Invalid")    

while True:
    print("Account details")
    print("Press 0 for logout")
    print("Press 1 for account details")
    print("Press 2 for deposit cash")
    print("Press 3 for withdraw cash")
    print("Press 4 for last 5 transactions")
    print("Press 5 for personal details")
    press=int(input("Press any number:"))
    bal=2000
    transactions=("dr.200 cr.500 cr.300 dr.1000 dr.100")
    name=("Mr.Raj, Savings Account")
    if press==0:
        print("Logout")
    elif press==1:
        print("Balance=",bal)
    elif press==2:
        d=int(input("Amount to be deposited:"))
        print("Bal=",bal+d)
    elif press==3:
        w=int(input("Amount to be withdraw:"))
        print("Bal=",bal-w)    
    elif press==4:
        print("Transactions=",transactions)
    elif press==5:
        print(name)
    else:
        print("Invalid")                              