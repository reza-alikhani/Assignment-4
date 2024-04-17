while True:
    number = int (input("enter a number greater than zero: "))

    m=1
    n=1

    while number >= m:
        
        m = m * n
        n = n + 1

        if number == m:
            print ("factorial")
            break
        elif number < m:
            print ("non-factorial")
            break
