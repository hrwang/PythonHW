
#### Promblem 1


    import math
    def find_roots (a,b,c):
        r1=(-b+math.sqrt(b**2-4*a*c))/2/a
        r2=(-b-math.sqrt(b**2-4*a*c))/2/a
        return(r1,r2)
    find_roots(1,-5.86,8.5408)




    (3.1400000000000006, 2.7199999999999998)



#### Problem 2


    for i in range(1,10):
        print 1.0/i #,"\n"

    1.0
    0.5
    0.333333333333
    0.25
    0.2
    0.166666666667
    0.142857142857
    0.125
    0.111111111111


#### Problem 3


    def triangular(n):
        sum=0
        for i in range(1,n+1):
            sum+=i
        return(sum)
    triangular(2)
    triangular(100)




    5050



#### Problem 4


    def factorial(n):
        sum=1
        for i in range(1,n+1):
            sum=i*sum
        #a="The factorial of"+ ' '+str(n) + ' '+"is:"+' '+ str(sum)+"."
        return sum
    print factorial(5)
    #factorial(100)

    120


#### Problem 5


    def backward(n):
        #a=
        for i in range(1,n+1):
            j=n-i+1
            return j
            #return factorial(j)
        
    backward(10)




    10




    n=10
    for i in range (1,n+1):
        j=n-i+1
        print factorial(j)

    3628800
    362880
    40320
    5040
    720
    120
    24
    6
    2
    1


#### Problem 6


    n=1
    sum=1
    for i in range (1,n+1):
        j=n-i+1
        sum+=factorial(j)
        #print factorial(j)
    print sum

    2



    print "%+10s %+20s" %("Julien", "Damien")

        Julien               Damien



    a="a string"
    a[0:6]




    'a stri'




    range?


    


    print "is English, isn't it?"

    is English, isn't it?



    print "is English, isn't it?"

    is English, isn't it?



    
