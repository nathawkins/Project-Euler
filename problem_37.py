def sieveOfAtkin(limit):
    ##Start with the formation of an array that holds the prime numbers
    P = [2,3]

    ##Make an array of Boolean's, all False to begin with, of length limit
    sieve=[False]*(limit+1)

    ##Now do the sifting, checking x values up until the sqrt(limit)
    for x in range(1,int((limit)**(1/2))+1):

        ##y values cover the same limits
        for y in range(1,int((limit)**(1/2))+1):

            '''
            All numbers with modulo-sixty remainder 1, 13, 17, 29, 37, 41, 49, or 53 have a modulo-twelve remainder of 1 or 5.
            '''
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5): ##If the value of n is divisible by 12 and has remainder 1 and 5
                sieve[n] = not sieve[n]           ##then flip the value of that entry in the sieve array.


            '''
            All numbers with modulo-sixty remainder 7, 19, 31, or 43 have a modulo-six remainder of 1.
            '''
            n = 3*x**2+y**2
            if n<= limit and n%12==7:             ##If the value of n is divisible by 12 and has a remainder of 7
                sieve[n] = not sieve[n]           ##then flip that value


            '''
            n needs to be a positive solution, so we have to check and make sure x is greater than y. All numbers with modulo-sixty remainder 11, 23, 47, or 59 have a modulo-twelve remainder of 11.
            '''
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:     ##If the value of n is divisible by 12 and has a remainder 11
                sieve[n] = not sieve[n]           ##then flip that value

    '''
    Now looking at the values, it's time to sieve them out. We know 2 and 3 are prime, so start at 5 (4 is not prime) and go until the sqrt of the limit. If that value in the sieve is True, then I can loop through the array and remove any perfect squares of that value. Thus eliminating any of the future prime numbers
    '''
    for x in range(5,int((limit)**(1/2))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False

    ##Build array of prime numbers
    for p in range(5,limit):
        if sieve[p]:
            P.append(p)

    return P

#Make list of primes separately!
limit = 1000000

all_primes = sieveOfAtkin(limit)
primes = all_primes[4:]
truncate_primes = []

# thefile = open('primes.txt', 'w')
#
# for i in all_primes:
#     thefile.write("{}\n".format(i))


# with open("primes.txt", "r") as file:
#     all_primes = file.readlines()
#
# all_primes = [int(x) for x in all_primes]
# primes = all_primes[4:]
# truncate_primes = []

def truncate_right(s):
    return s[:-1]

def truncate_left(s):
    return s[1:]


for i in range(len(primes)):
    p = str(primes[i])
    broken = False
    while len(p) > 1 and not broken:
        p = truncate_left(p)
        if int(p) in all_primes:
            continue
        else:
            broken = True

    if not broken:
        p = str(primes[i])
        while len(p) > 1 and not broken:
            p = truncate_right(p)
            if int(p) in all_primes:
                continue
            else:
                broken = True
    else:
        continue

    if not broken:
        truncate_primes.append(primes[i])
    else:
        continue

print(len(truncate_primes))
print(truncate_primes)
print(sum(truncate_primes))
