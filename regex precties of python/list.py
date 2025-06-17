# # Create a list
# fruits = ["apple", "banana", "cherry"]

# # Add an item to the end
# fruits.append("date")
# print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# # Insert an item at a specific position
# fruits.insert(1, "blueberry")
# print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date']

# # Remove an item by value
# fruits.remove("banana")
# print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# # Remove an item by index and get its value
# popped = fruits.pop(2)
# print(popped)  # 'cherry'
# print(fruits)  # ['apple', 'blueberry', 'date']

# # Find the index of an item
# index = fruits.index("date")
# print(index)  # 2

# # Count how many times an item appears
# count = fruits.count("apple")
# print(count)  # 1

# # Sort the list
# fruits.sort()
# print(fruits)  # ['apple', 'blueberry', 'date']

# # Reverse the list
# fruits.reverse()
# print(fruits)  # ['date', 'blueberry', 'apple']

# # Clear all items
# fruits.clear()
# print(fruits)  # []

# print(len(fruits))



# list=[1,23,43,21,2,3,5,4231,132,5664]
# list1=[]
# for i in range(0,len(list)):
#     if list[i]%2==0:
#         list1.append(list[i])
# print(list1)





# quetion 1
# 

# first way
# list=[23,43,21,2,3,5,132,23332,432,321,9999999,]
# highest=list[0]

# for i in range(0,len(list)):
    
#     if list[i]>highest:
#         highest=list[i]


# secondHigest=list[0]
# for i in range(0,len(list)):
    
#     if list[i]>secondHigest and list[i]<highest:
#         secondHigest=list[i]
# print(secondHigest)







# quetion 2

# list=[23,43,21,2,3,5,"abc","sd",2,43,]
# highest=list[0]

# for i in range(0,len(list)):
    
#     if type(list[i])==int:
#        print(list[i])





# # quetion 3

# list=[23,43,21,2,3,5,2,43,]
# total=0

# for i in range(0,len(list)):
    
#     total=total+list[i]
# print(total)




# quetion 4

# list=[10,43,21,2,3,5,2,43,]


# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         print(f"{list[i]}  :  {list[j]}")



# quetion 5


# list=[10,43,21,2,3,5,2,43]

# j=len(list)-1
# i=0
# while i<j:
#     temp=list[i]
#     list[i]=list[j]
#     list[j]=temp
#     i+=1
#     j-=1


# print(list)
    


# quetion 6


# list=[1,2,2,2,2,2,2,3,3,3,4,5,6,6,6,6,7]
# temp=list[0]
# for i in range(1,len(list)):
#     if temp==list[i]:
#         print(temp)
#         print(list[i])
        
#         list.pop(i)
#     else:
#         temp=list[i]


    


# print(list)
    



# quetion :7 Write a Python program to reverse a list without reverse or slicing operator


# list=[1,2,2,2,2,2,2,3,3,3,4,5,6,6,6,6,7]
# i=0
# j=len(list)-1
# while i<j:
#     temp=list[i]
#     list[i]=list[j]
#     list[j]=temp
#     i+=1
#     j-=1


# print(list)



# quetion :8 Sort list in ascending order without sort()


# list=[9,8,7,11,4,3,2,1]
# i=0
# j=1

# while i<len(list)-1:
#     if list[i]>list[j]:
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
#     if j==len(list)-1 :
#          i+=1
#          j=i+1
#     else:
#          j+=1
        
    

# print(list)




# quetion :9     Remove duplicates while keeping order


# list = [1, 2, 2, 3, 4, 4, 5]
# i=0
# while i<len(list)-1:
#     if list[i]==list[i+1]:
#         list.remove(list[i+1])
#     i+=1
        
# print("List after removing duplicates:", list)








# quetion  10 Find pairs that sum to target


# list = [1, 2, 2, 3, 4, 4, 6,8,5,3]
# taupleOfList=[]
# target=6
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         print(list[i],list[j])
#         if(list[i]+list[j]==target):
#             print(list[i],list[j])
#             taupleOfList.append((list[i],list[j]))
        
# print(taupleOfList)






# # quetion  11  Sum excluding largest and smallest (no max/min)


# # list = [1, 2, 3,  4, 6,8,5,3]
# list=[1,2,3,4,5]
# largest=list[0]
# smallest=list[0]
# sum=0
# for i in range(0,len(list)):
#     # print(largest,smallest)
#     if largest<list[i] :
#         largest=list[i]
#     if list[i]<smallest:  
#         print(smallest,list[i])      
#         smallest=list[i]
#     sum=sum+list[i]

# print(largest)
# print(smallest)

# sum=sum-largest-smallest 
        
# print(sum)











# quetion  12  Sum excluding largest and smallest (no max/min)



# list=[]
# templist=[]
# num=9
# for i in range(0,num):
#     for j in range(0,i+1):
      
#         if j==0 or j==i:
#             templist.append(1)
            
#         else:
#             t=list[i-1][j]+list[i-1][j-1]
#             templist.append(t)
            
    
#     list.append(templist)
#     templist=[]
# print(list)
   











# list comphrehension


# list=[ [i,j] for i in range (1,5)  for j in range(1,5)]
# print(list)









# q:13 two number sum == total

# list=[-1,0,1,13,14,16]
# total=12
# i=0
# j=1
# while(i<j):
#     if list[i]+list[j]==total :
#         print(i,j)
#         break
#     elif list[i]+list[j]<total:
#         i+=1
#         j+=1
#     elif list[i]+list[j]>total:
#         i-=1
        
    





# q:14 valid parentheses 


parentheses = input("Enter a string of parentheses: ")
i=0
j=1
valid=True
while j<len(parentheses):

    if parentheses[i]=="(" or parentheses[i]=="(" :
         if ord(parentheses[i])!=ord(parentheses[j])-1:
             valid=False
    else:
         if ord(parentheses[i])!=ord(parentheses[j])-2:
             valid=False

    i+=2
    j+=2

print(valid)


