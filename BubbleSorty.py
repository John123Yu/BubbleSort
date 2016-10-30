from random import randint
import datetime
x = []
done = 0

for num in range(0,100):
	randomNumber = randint(0,10000) 
	x.append(randomNumber)

start = datetime.datetime.now()

for j in range(0,len(x)-1):
	for i in range(1,len(x)-done):
		if x[i-1] > x[i]:
			temp = x[i]
			x[i] = x[i-1]
			x[i-1] = temp
	done += 1
print x

end = datetime.datetime.now()
SortTime = end - start
print SortTime