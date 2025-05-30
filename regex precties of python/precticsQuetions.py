# question-1
num=2
count=0
while count<=3:
    isprime=True
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    if isprime:
        print(num, end=" ")
        count+=1
    num+=1


    #quetion -2
    count=0
    i=1
    while count<50:
        if(i%2==0 and i%3==0 and i%6==0):
            print(i)
            count+=1
        i+=1


