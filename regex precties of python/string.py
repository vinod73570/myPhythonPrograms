


# q. 
# take a string and check 
# the string should have 1 capital later
# altest 1 small
# 1 num,
# minimimlen of 6 char


# s="Vinod9"
# dict={"capital":False,"small": False,"num":False,"length":False}
# for i in range(0,len(s)):
#     if 65<=ord(s[i])<=90:
#         dict["capital"]=True
#     if 97<=ord(s[i])<=112:
#         dict["small"]=True
#     if "0"<=s[i]<="9":
       
#         dict["num"]=True
# if(len(s)<=6):
#     dict["length"]=True  

# if(all(dict.values())) :
#     print("valid")
# else:
#     print("no")






# que : reerse string 


a=" my name is vinod  "
list=[]
reverseString=" "
temp=""
for i in range(0,len(a)):
    temp=temp+a[i]
    if(a[i]==" "):
        # temp=temp+a[i]
        list.append(temp)
        temp=""
for i in range(len(list)-1,-1,-1):
    reverseString=reverseString+list[i]+" "


print(reverseString)


