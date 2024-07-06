def generate_fibonacci(num):
    a = 0
    b = 1

    if num == 0:
        print(a)

    else:
        print(a)
        print(b)

    for i in range (2,num+1):
        c = a + b
        a = b
        b = c

        print(c)

while True:
    num = int(input("Enter a number to obtain fibonacci sequence: "))
    generate_fibonacci(num)





    