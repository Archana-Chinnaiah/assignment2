#number of ways to find whether a key exists in a dictionary or not



'''METHOD-1'''


# Python3 Program to check whether a given key already exists in a dictionary. 
#keys()
fruits = dict()
n=3
i=0
while i<n:
 names = input("Enter the fruit name: ")
 quantity = input("Enter the quantity: ")
 fruits[names] = quantity
 i=i+1
ch=input("enter the key to check")
print(ch in fruits.keys())


'''METHOD-2'''


# Python3 Program to check whether a given key already exists in a dictionary. 
#in
fruits = dict()
n=2
i=0
while i< n:
 names = input("Enter the fruit name: ")
 quantity = input("Enter the quantity: ")
 fruits[names] = quantity
 i=i+1
ch=input("enter the key to check")
if ch in fruits:
    print ("key already exsists")
else:
    print ("key  not exsists already")


'''METHOD-3'''


# Python3 Program to check whether a given key already exists in a dictionar
# using get mathod 
fruits = dict()
n=5
i=0
while i< n:
 names = input("Enter the fruit name: ")
 quantity = input("Enter the quantity: ")
 fruits[names] = quantity
 i=i+1
print(fruits.get('mango'))


    
