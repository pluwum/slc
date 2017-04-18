#check if number is a prime
def isPrime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    else:
        return True


#return list of primes from 0 to number
def primes(number):
	primes = []
	
	if number >= 0:
		for x in range(2, number+1):
			if(isPrime(x)):
				primes.append(x)
		return primes
	else:
		raise ValueError	

#mic check 1..2..3
#print (primes(20))