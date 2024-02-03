# def leap_year(year):
#     x=int(input("Enter year:"))
#     if x%4==0:
#         return True
#         # print(x,"is a leap year")
#     else:
#         return False
#         # print(x,"is a Non leap year")

# x=5
# a=str(x)
# print(type(a))

class InterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def simple_interest(self):
        return (self.principal * self.rate * self.time) / 100

    def compound_interest(self):
        return self.principal * ((1 + (self.rate / 100)) ** self.time) - self.principal