# print("hi")
# n=int(input("Enter any number:"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")    
    
# x=int(input("Enter your age:"))
# if x>=16:
#     if x>=18:
#         print("You are eligible for license")
#     else:
#         print("You are not eligible for license")
# else:
#     print("You are not eligible for learning license")    

n=int(input("Enter any number..."))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")    
    print()