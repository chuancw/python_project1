path='E:\python_code\\test.txt'
f_name=open(path)
print(f_name.name)

f_name.close()

f_name=open(path,'r')
print(f_name.read(12))
f_name.close()












