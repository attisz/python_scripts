
def Is_prime(n):
	if n < 2:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def Dividents(n):
	return [x for x in range(1, n + 1) if n % x == 0]


#########################################################

def Is_congruent(a, b, M):
	return a % M == b % M

def Primes_d_mod_M(a,b,d,M):
	if a > b:
		raise ValueError("invalid range definition") 
	return [x for x in range(a, b) if Is_prime(x) and Is_congruent(x, d, M)]

########################################################

def Prime_dividents(n):
	return [x for x in Dividents(n) if Is_prime(x)]

def Series(n):
	list = [n]

	if Is_prime(n):
		return list

	s = sum(Prime_dividents(n))

	while True:
		list.append(s)
		if Is_prime(s):
			return list
		s = sum(Prime_dividents(s))

#########################################################

def Is_square_number(n):
	for i in range(1, n + 1):
		if i ** 2 == n:
			return True
	return False

def Sqare_number_dividents(n):
	return [x for x in Dividents(n) if Is_square_number(x)]

def Create_graph(m):
	return [(v,e) for v in range(1, m + 1) for e in range(1, m + 1) if v != e and sum(Sqare_number_dividents(v)) == sum(Sqare_number_dividents(e))]

#########################################################

try:
	print(Primes_d_mod_M(1,0,3,10))
except ValueError as e:
	print(e)

print(Primes_d_mod_M(0,0,3,10))
print(Primes_d_mod_M(0,100,3,10))

print('---------------')

for n in range(1000, 1010):
	print(Series(n))

print(Create_graph(10))

m = int(input("Enter m:"))
print(Create_graph(m))




