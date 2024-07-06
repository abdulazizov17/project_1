# bunisi range ga misol
# def all_primes(N):
#     primes = []
#     for n in range(2, N+1):
#         is_n_prime = True
#         for p in primes:
#             if n%p == 0:
#                 is_n_prime = False
#                 break
#         if is_n_prime:
#             primes.append(n)
#             yield n
# for p in all_primes(50):
#     print(p)
    
# bunisi itaratorga misol

def tub_son_topish(n):
    tub_sonlar = []
    for num in range(2, n + 1):
        is_tub = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_tub = False
                break
        if is_tub:
            tub_sonlar.append(num)
    return tub_sonlar
n = 50
tub_sonlar = tub_son_topish(n)
print(f"{n} gacha tub sonlar: {tub_sonlar}")

        
    