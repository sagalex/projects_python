def fib(n):
   a:int 
   b:int = 0, 1
   while a < n:
      print(a, end=' ')
      a, b = b, a+b
      print()
   fib(1000)