# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:01:21 2021

@author: Bbatd
"""

def c():
	max = maxI = maxJ = 0
	i = 999
	j = 990
	while (i > 100):
		j = 990
		while (j > 100):
			product = i * j
			if (product > max):
				productString = str(product)
				if (productString == productString[::-1]):
					max = product
					maxI = i
					maxJ = j
			j -= 11
		i -= 1
	return max, maxI, maxJ


print(c())