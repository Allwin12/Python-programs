def fibonacci(limit):
    a,b = 0,1
    while(limit):
        print(a)
        a,b = b,a+b
        limit=limit-1

print("this is the fibanocci series program")
limit  = int(input("Enter the limit"))
fibonacci(limit)
