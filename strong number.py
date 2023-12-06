x=int(input("give the number: "))
a=len(str(x))
c=x
sum=0
while x!=0:
    num=x%10
    fact=1
    
    for j in range(1,num+1):
        fact=fact*j
    sum=sum+fact
    x=x//10

print(sum)
if c==sum:
    print("yes")
else:
    print("no")
