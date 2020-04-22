
def num(a):
    i = 0
    if a % 2 == 0:
        gugudan_even()
    else: 
        gugudan_odd()

def gugudan_even():
    i = 0
    j = 0
    for i in range(1,10):
        for j in range(1,10):
            if i % 2 == 0:
                print("%d x %d = %d" % (i,j,i*j))
def gugudan_odd():
    i = 0
    j = 0
    for i in range(1,10):
        if i % 2 == 1:
            for j in range(1,10):
                print("%d x %d = %d" % (i,j,i*j))
num(3)