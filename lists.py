color=['red','blue','black','green']
print(color)
age=[7,9,3,4,5,9]
print(age[-1])
print('23' in age)

empty=[]
print(2 in empty)

num1=[1,2,3,4]
num2=[3,7,8,9]
num3=num1+num2
print(num3)
num4=num3*2
print(num4)
for i in num3:
    print(i*2)

#printing all values
cs_performance=[56,98,78,65,76,85]
first_3=cs_performance[:]
print(first_3)
#replacing values
cs_performance[1:3]=[45,66]
#adding an element at the end
cs_performance.append(87)
print(cs_performance)
#deleting the last element
cs_performance.pop()
print(cs_performance)
#removing an item
cs_performance.remove(66)
del cs_performance[3]
print(cs_performance)
#printing sum
print(sum(cs_performance))
#inserting items
cs_performance.insert(49,35)
print(cs_performance)










