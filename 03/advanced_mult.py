#!/usr/bin/env python3
n = 0
i = 0
while (n < 11):
	print(f"Table of {n}: ", end= " ")
	while (i < 11):
		print(n * i, end=" ")
		i += 1
	n += 1
	i = 0
	print()
