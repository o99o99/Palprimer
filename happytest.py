print("NOW HAPPY PALPRIMES:")

def digits(n):
  if n == 0:
    return []
  else:
    return digits(n // 10) + [n % 10]

digit_squares = [n*n for n in range(0, 10)]
end_loop = [4, 16, 37, 58, 89, 145, 42, 20]

primeslist = range(1, 1000)

for item in primeslist:
  i = item
  while i not in [1] + end_loop:
    i = sum([digit_squares[d] for d in digits(i)])
  if i == 1:
    print item

