def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def count_primes(L,R):
    primes=[]
    for i in range(L,R+1):
        if is_prime(i):
            primes.append(i)
    count = len(primes)
    print("Primes:", primes)
    return count

L, R = 10, 30
print(f"Total primes between {L} and {R}:",count_primes(L, R))