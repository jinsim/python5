def gugudan(n):
    i = 1
    j = 1
    while i < n:
        i+=1
        for j in range(1,10):
            print("%d x %d = %d" % (i, j, i*j)) 
gugudan(3)