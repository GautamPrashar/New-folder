# a={"second","minute","hour","day","week","month","year","era"}
# print(a)
# print(type(a))
# for i in a:
#     print(i)
# a.update(["decade"])  
# print(a) 
# a.add("decade")
# print(a)
# a.remove("second")
# a.discard("hour")
# print(a)
# b={"jan","feb","march"}
# print(a|b)

x={1,2,3,4}
y={2,4,6,7}
z={1,2,4,7,10}
# print(x|y|z)
# print(x.union(y,z))
# print(x&y&z)
print(x-y)
print(x-y-z)
print(x^y^z)