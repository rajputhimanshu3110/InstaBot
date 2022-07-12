num = [x for x in range(2,101)]
x,j=2,0
while (x**2<100):
    for i in num:
        if i>x and i%x==0:
            num.remove(i)
    j=j+1
    x=num[j]
print(num)
print(j)
print(num[j])
