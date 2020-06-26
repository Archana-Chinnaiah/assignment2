List = []
Number = int(input("enter no.of.List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d list : " %i))
    List.append(value)
List.sort()

print("Element After Sorting List in Ascending Order is : ",List)
