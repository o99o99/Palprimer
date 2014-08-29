import math, time
bottomrange = int(input("Enter the bottom number: "))
toprange = int(input("Enter the top number: "))
primeslist = []
palprimeslist = []
hpalprimeslist = []
print("PRIMES FOR THAT RANGE:")
time.sleep(1)
try:
    for i in range (bottomrange,toprange):
        num = i
        for i in range(2,int(math.sqrt(num))):
           if (num % i) == 0:
               break
        else:
            print(num)
            primeslist.append(num)
except KeyboardInterrupt:
    time.sleep(1)
    print()
    print("HALTED. ALL FURTHER LISTS WILL ONLY INCLUDE NUMBERS ABOVE.")
    time.sleep(1)
print("THAT'S A TOTAL OF:")
time.sleep(1)
print(len(primeslist))
time.sleep(1)
print("OF THOSE, THESE ARE PALPRIMES:")
time.sleep(1)
try:
    for item in primeslist:
        if str(item) != str(item)[::-1] or item<10:
            pass
        else:
            print(item)
            palprimeslist.append(item)
except KeyboardInterrupt:
    print()
    time.sleep(1)
    print("HALTED. ALL FURTHER LISTS WILL ONLY INCLUDE NUMBERS ABOVE.")
    time.sleep(1)        
print("THAT'S A TOTAL OF:")
time.sleep(1)
print(len(palprimeslist))
time.sleep(1)
print("NOW HAPPY PALPRIMES:")
try:
    time.sleep(1)
    def digits(n):
      if n == 0:
        return []
      else:
        return digits(n // 10) + [n % 10]
    digit_squares = [n*n for n in range(0, 10)]
    end_loop = [4, 16, 37, 58, 89, 145, 42, 20]
    for item in palprimeslist:
      i = item
      while i not in [1] + end_loop:
        i = sum([digit_squares[d] for d in digits(i)])
      if i == 1:
        print(item)
except KeyboardInterrupt:
    time.sleep(1)
    print()
    print("HALTED")
time.sleep(1)              
input("Press to exit")
       
       
   

       
       
   
