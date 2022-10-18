import re
#a = '''asdfhellopass:
#    worldaf
#       '''
#b = re.findall('hello(.*?)world',a)
#c = re.findall('hello(.*?)world',a,re.S)
#print('b is',b)
#print('c is',c)

#res = re.findall(r"A","abc",re.I)
#print(res)

s = '12 34 \n56 78 \n90'
res1 = re.findall(r'^\d+', s, re.M)
res2 = re.findall(r'\A\d+', s, re.M)
res3 = re.findall(r'\d+$', s, re.M)
res4 = re.findall(r'\d+\Z', s, re.M)

print(res1)
print(res2)
print(res3)
print(res4)


I = ['1 2','2 3','3 4']
print(eval(re.sub(r'\s*','',str(I))))




