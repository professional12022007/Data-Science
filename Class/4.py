import numpy as np



# # a = np.array([1,2,34,4,5,45,65,34,3,233,5465,76,6,745,45])

# # print(a)
# # question 2
# # np_arr=np.array([3,3,3,3,3,3,3,'hello',False])
# # print(bool(np_arr[-1]))
# # a=False
# # print(bool(a))

# # a=np.zeros((2,5))          #parameters for 2 array are given in the form of the list or the tupple 
# # print(a)


# # a=np.zeros((2,5,4),dtype=int)          
# # print(a)
# # print(type(a[0][0][0]))



# # a=np.ones((2,5,4),dtype=int)          
# # print(a)
# # print(type(a[0][0][0]))


# # a=np.empty(4,dtype=int)          
# # print(a)



# # a=np.full(4,5,dtype=int)          
# # print(a)

# # a=np.arange(5,24,1,dtype=int)
# # print(a)  


# # a=np.linspace(5,24,123)
# # print(a) 



# # a = np.array([1, 2, 3, 4, 5])

# # print(a.shape)

# # b = np.array([
# #     [1, 2, 3],
# #     [4, 5, 6]
# # ])

# # print(b.shape)

# # vass = np.array([
# #     [1, 2, 3],
# #     [4, 5, 6]
# # ])

# # print(vass.size)

# # va = np.zeros((2, 3, 4))

# # print(va.shape)
# # print(va.size)



# # a = np.array([1, 2, 3, 4, 5])

# # b=np.array([21,223,45,4,65])
# # print(a*b)
# # print(a+b)
# # print(a-b)
# # print(a/b)
# # print(a%b)
# # print(a^b)


# # lst = [np.random.randint(1, 100) for _ in range(10)]
# # a=np.random.randint(2,312,6)
# # print(a)
# # print(lst)

# # a = np.arange(9)

# # print(a)


# # b = a.reshape(3, 3)

# # print(b)
# # n=b.transpose()
# # print(n)


# # c = np.concatenate((n, b), axis=1)

# # print(c)

# # a=np.random.randint(2,15,6)
# # b=np.random.randint(1,19,6)
# # print(a)
# # print(b)
# # c=np.where(b>2,b,a)
# # print(c)


# arr = np.array([10, 20, 30, 40, 50])

# result = np.where(arr > 25, 1, 0)
# print(result)


# arr = np.array([40, 10, 30, 20])

# print(np.sort(arr))


# arr = np.array([[3,1],[4,2]])

# print(np.sort(arr))

# arr = np.array([1,2,3,4])

# print(np.sum(arr))

# arr = np.array([[1,2],[3,4]])

# print(np.sum(arr, axis=1))


# arr = np.array([[1,5],[3,2]])

# print(np.min(arr, axis=0))


# arr = np.array([10, 5, 20, 2])

# print(np.max(arr))


# arr = np.array([1,2,3,4,5])

# print(np.std(arr))


# arr = np.array([1,2,2,3,3,3,4])

# print(np.unique(arr))


# n=input("Enter list separated by spaces: ")
# vass1 = [int(num) for num in n.split()]
# vass=np.array(vass1)
# monday=vass[0]
# tuesday=vass[1]
# wednesday=vass[2]
# thursday=vass[3]
# friday=vass[4]
# saturday=vass[5]
# sunday=vass[6]
# print(vass)
# print(np.max(vass))
# print(np.mean(vass))
# print(np.std(vass))
# print(np.min(vass))
# print(np.unique(vass))
# print(np.sort(vass))


# home work 
# explore other functions in the numpy
# explore the concept of copy in python 
# price input of a grocery shop and run all these functions


# homework


# items = []
# prices = []

# for i in range(7):
#     name = input(f"Enter name of item {i+1}: ")
#     price = float(input(f"Enter price of {name}: "))

#     items.append(name)
#     prices.append(price)

# prices = np.array(prices)


# max_price = np.max(prices)
# min_price = np.min(prices)
# mean_price = np.mean(prices)
# std_price = np.std(prices)


# max_item = items[np.argmax(prices)]
# min_item = items[np.argmin(prices)]


# print("\n----- Results -----")
# print(f"Most expensive item : {max_item} (₹{max_price})")
# print(f"Cheapest item       : {min_item} (₹{min_price})")
# print(f"Average price       : ₹{mean_price:.2f}")
# print(f"Standard Deviation  : ₹{std_price:.2f}")



# a= np.random.randint(1,90,25)
# x=a.reshape(5,5)
# print(x)
# # finding the mean of the matrix row wise and the column wise 
# mean=np.mean(x,axis=1)
# print(mean)
# mean=np.mean(x,axis=0)
# print(mean)
# # replacing the even number with the -1
# sot=np.where(x%2==0,-1,x)
# print(sot)
# # sort the array row wise and the coloumn wise 
# sor=np.sort(sot,axis=0)
# print(sor)
# sor=np.sort(sot,axis=1)
# print(sor)
# # find the row wise and the column wise sum
# sum=np.sum(x,axis=0)
# print(sum)
# sum=np.sum(x,axis=1)
# print(sum)
# # for counting the number of -ve the each coloumns 
# # num=np.sum(sot<0,axis=0)
# # print(num)
# # or
# num=np.sum(np.where(x<0,1,0),axis=0)
# print(num)


# inventery control system 
a= np.random.randint(20,80,25,dtype=int)
stock=a.reshape(5,5)
a= np.random.randint(20,80,25,dtype=int)
demand=a.reshape(5,5)
# remaining stock = stock - demand
remaining_stock=stock-demand
print(remaining_stock)
# finding the total shortage 
shortage= np.sum(np.where(remaining_stock>0,0,remaining_stock))
print(shortage)

# replacing the -ve values with the 0
sot=np.where(remaining_stock<0,0,remaining_stock)
print(sot)
# finding the sum of the products with the shortage
num=np.sum(np.where(sot==0,1,0),axis=0)
print(num)
total=np.sum(num)
print(total)

# sort the array row wise and the coloumn wise 
sor=np.sort(sot,axis=0)
print(sor)
sor=np.sort(sot,axis=1)
print(sor)
