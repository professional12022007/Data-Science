# lst=[1,23,3.4343,545665,2324]
# lst.append(32)
# print(lst)
# print(lst.index(23))
# lst.sort()
# print(lst)
# vass=[21,23,435,65,5,76,878,756,45,34,34454,6,76767,8]
# print(sorted(vass))
# print(min(vass))
# print(max(vass))
# vass=(12,212,3223,43243,54,65,76,587876,453,3,2,1)
# print(vass.count(2))
# print(vass.index(2))
# print(len(vass))
# print(sum(vass))
# print(max(vass))
# print(min(vass))





n=input("Enter 1st list separated by spaces: ")
m=input("Enter 2nd list separated by spaces: ")
vass1 = [int(num) for num in n.split()]
vass2=[int(num) for num in m.split()]
vass3=[]
for i in range(len(vass1)):
    vass3.append(vass1[i]+vass2[i])

print(vass3)

