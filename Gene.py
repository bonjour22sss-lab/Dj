e=" "
s=" "
j=0
i=0
b=[]
a=["a","p"]
aa=[]
c=[]


for i in range(26):
	e=chr(97+i)
	aa.append(e)


for i in aa:
	for j in aa:
		for k in aa:
			e=i+ "_" + j + "_" + k
			c.append(e)
			print(e)

				
# print("\nlenth is:"  ,len(c) )
