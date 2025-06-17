# student = {
#     "name": "Vinod",
#     "course": "Python",
#     "score": 95
# }

# # Access
# print(student["name"])  # Vinod

# # Add
# student["email"] = "vinod@example.com"

# # Update
# student["score"] = 98

# print(student.items())


# Loop
# for k, v in student.items():
#     print(k, v)








# my_dict = {"name": "Vinod", "age": 25}

# items_view = list(my_dict.items())
# print(items_view)  
# my_dict["city"] = "Jaipur"
# print(items_view)  # dict_items([('name', 'Vinod'), ('age', 25), ('city', 'Jaipur')])
# items_view["name"]="vinodddd"
# print(items_view)







# my_dict = {"name": "Vinod", "age": 25}
# count=1
# for k, v in my_dict.items():  # convert to list to avoid "dictionary changed size" error
#     # if k == "name":
#     print(count)
    
#     my_dict["username"] = v  # add new key
#         # del my_dict[k]          # delete old key
#     count+=1

# print(my_dict)









# quetions for precties 



# q.1   Count how many times each item appears in a list.


# list=["vinod","vinod","jat","jat","vinod","is","is","vinod","vinod","is","is","is"]
# dict={}

# for i in range(0,len(list)):
#     if list[i] in dict:
#         dict[list[i]]=dict[list[i]]+1
#     else:
#         dict[list[i]]=1
# print(dict)

#second way 

# list=["vinod","vinod","jat","jat","vinod","is","is","vinod","vinod","is","is","is"]
# dict={}

# for i in list:
#     if i in dict:
#         dict[i]=dict[i]+1
#     else:
#         dict[i]=1
# print(dict)
        






#  q.2   

# s="abc"
# dict={}
# i=0
# k=i+1
# j=0
# while i<3:
#     data=" "
#     j=i
#     if k<=3:
#         while j<k:
#         # print(s[j])
#          data=data+s[j]
#          j+=1
    
#     k+=1

#     if k>3:
#         i+=1
#         k=i+1
#     if data in dict:
#         dict[data]=dict[data]+1
#     else:
#         dict[data]=1
        
 
         
# print(dict)
        








# q 3

# a="GHARD"
# for i in range(0,5):
#     d=ord("A")
#     char=a[i]
#     char = ord(char)
#     d=char-d
    
#     print(chr(90-d))








# q.4

# list=[0,1,2,4,7,11,14,15]
# target=9
# dict={}

# for i,v in enumerate(list):
#     dict[v]=i
# for i in list:
#     if target-i in dict:
#         print(dict[target-i])

        
        
        




# # q.5
# dict={1:"I",4:"IV",5:"V",9:"IX",10:"X", 50:"L", 100:"C",500:"D",1000:"M",40:"XL",90:"XC",400:"CD",900:"CM"}    #panding
# number=19
# romen=""
# while number!=0:
#     if number in dict:
#         romen=romen+dict[number]
#     else:
       
#         r=number%10
#         while r!=0:
#              if r in dict:
#                  romen=romen+dict[number]
#                  r=0
#              if 1<=r<4:
#                   romen=romen+dict[1]
#                   r=r-1
#              elif 5<r<9:
#                  romen=romen+dict[5]
                 




vinod_skills = {"Python", "React", "HTML"}
friend_skills = {"Java", "React", "Python"}

print("\n🎯 8. union() – Combine both skillsets")
all_skills = vinod_skills.union(friend_skills)
print("All skills (combined):", all_skills)
















# dict comphrehension


dict={i:i**2 for i in range(1,12)}
print(dict)