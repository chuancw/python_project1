print(sorted([36,7,8,9]))

print(sorted([36, -34, 1,-6, 7], key=abs))

print(sorted(['A', 'c','B','Z','x']))
print(sorted(['A', 'c','B','Z','x'], reverse=True))
print(sorted(['A', 'c','B','Z','x'], key=str.lower))




# 排序小练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(list):
    return list[0]

def by_score(list):
    return -list[1]

L_by_name = sorted(L, key=by_name)
print(L_by_name)
L_by_score = sorted(L, key=by_score)
print(L_by_score)