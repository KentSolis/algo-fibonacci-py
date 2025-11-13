def fibonacci(n):
    #first I place my base cases, for if n <= 0 || n = 1
   if n < 0:
      return "Incorrect input"
   elif n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)