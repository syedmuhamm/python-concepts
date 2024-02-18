# Simultanous assignments in Python, used twice
a , b = 0 ,1
while(a < 10):
    print(a)
    a, b = b, a+b
   
