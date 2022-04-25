str1="建筑信息模型 is BIM 2022"
res1=str1[2]+str1[3]+str1[9]+"Info"
res2=(str1[10]+str1[11]+str1[12])*3
res3=len(str1)*str1[14]
str2='HELLO revit'
res4=len(str2)
res5="BIM:REVIT"
res6=bool('')
res7=int('10')*'*'
res8=float('5.0')+5.0

print(res1)  # 信息 Info
print(res2)  # BIMBIMBIM
print(res3)  # 222222222222222222
print(res4)  # 11
print(res5)  # BIM:REVIT
print(res6)  # False
print(res7)  # **********
print(res8)  # 10.0