# class interestcalculation:
#     def __init__(self,p,r,t):
#         self.p=p
#         self.r=r
#         self.t=t
#     def calculate_interest(self):
#         return(self.p*self.r*self.t)/100
#     p=int(input("Enter principle="))
#     r=int(input("Enter rate="))
#     t=int(input("Enter time="))
#     print(calculate_interest)
if __name__ == '__main__':
    n = int(input("enter"))
    arr = map(int, input().split())
    a=set(arr)
    b=sorted(a)
    print(b[-2])