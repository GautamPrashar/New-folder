# n=int(input("enter number:"))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()
    

# n=int(input("Enter="))
# c="*"
# for i in range(n):
#     print((c*i).rjust(n-1)+c+(c*i).ljust(n-1))






# thickness = int(input())
# c = 'H'
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# for i in range(thickness+1):  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# for i in range(thickness):  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))







# n=int(input("Enter="))
# m=(n*3)-2
# for i in range(0,n):
#     for j in range(0,m):
#         print(end=" ")
#     m=m-1
#     for j in range(0,i+1):
#         print(".|.",end=" ")
#     print("")

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
for i in range(n//2):
    j=int((2*i)+1)
    print((j*".|.").center(m,"-"))
print(("WELCOME").center(m,"-"))
for i in reversed(range(n//2)):
    j=int((2*i)+1)
    print((j*".|.").center(m,"-"))