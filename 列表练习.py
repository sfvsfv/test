x=10
y=3
z='m'
res1=[x,y,z]
res2=[x+y,x*y,str(x)+z]
res3=res1+res2
res4=res1*2
res4[3]=15
res4[4]=5
res4[5]='M'
res5=res4
res6=res3+res4
res7=res5[-1]
res8=res5[-2]
res9=bool([])

print(res1)  # [10, 3, 'm']
print(res2)  # [13, 30, '10m']
print(res3)  # [10, 3, 'm', 13, 30, '10m']
print(res4)  # [10, 3, 'm', 15, 5, 'M']
print(res5)  # [10, 3, 'm', 15, 5, 'M']
print(res6)  # [10, 3, 'm', 13, 30, '10m', 10, 3, 'm', 15, 5, 'M']
print(res7)  # M
print(res8)  # 5
print(res9)  # False