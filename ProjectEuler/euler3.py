#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number = 13195
largestPrime = 0
prime = 0

for x in range(1,number):
	for y in range(2, x - 1):
		prime = 0
		if x % y == 0:
			prime = 0
		else:
			prime = 1
	if prime == 1:
		largestPrime = x
print str(largestPrime)
