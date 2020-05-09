import femurtotall

key = float(input("값을 입력해주세요 : "))

print("입력받은 값 : ", key)

result1 = femurtotall.M_pearson(key)
result2 = femurtotall.M_Trotter(key)
result3 = femurtotall.M_huzii(key)
result4 = femurtotall.F_pearson(key)
result5 = femurtotall.F_huzii(key)

print("Male Pearson : ", result1)
print("Male Trotter&Glaser : ", result2)
print("Male huzii : ", result3)
print("Female Pearson : ", result4)
print("Female huzii : ", result5)
