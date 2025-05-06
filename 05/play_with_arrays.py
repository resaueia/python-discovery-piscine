#!/usr/bin/env python3

n1 = [2, 4, 8, 10, 12]
print(n1)
res = []
i = 0
while (i < len(n1)): 
	if (n1[i] > 5):
		res.append(n1[i] + 2)
	i += 1
print(res)

#or, much simpler, i could've done this:

##!/usr/bin/env python3

# play_with_arrays.py – process only values > 5

#n1 = [2, 8, 9, 48, 8, 22, -12, 2]
#print(n1)
# filter-and-transform in one go
#result = [x + 2 for x in n1 if x > 5]
#print(result)



