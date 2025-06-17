
Nested_list=[1,[2,3],4,5,[6,[7,8],9],10]
temp=Nested_list[::-1]
ans=[]
while temp:
    value=temp.pop()
    if isinstance(value,list):
        temp.extend(value[::-1])
    else:
        ans.append(value)

print(ans)





