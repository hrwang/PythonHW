
# Stat 133: Homework 5 (Deadline: October 12, 4 a.m.)

##Reading assignment from [A Primer on Scientific Programming with
Python](http://link.springer.com/book/10.1007/978-3-642-18366-9/page/1):

* **Section 5.1**: Vectors
* **Section 5.2**: Array in Python Programs
* **Section 5.6.1**: Copying Arrays
* **Section 5.6.3**: Allocating Arrays
* **Section 5.6.7**: Shape Manipulation
* **Section 5.7**: Higer-Dimensional algebra

* Read and play with the notebook
[here](http://nbviewer.ipython.org/urls/raw.github.com/jrjohansson/scientific-
python-lectures/master/Lecture-4-Matplotlib.ipynb) that will teach you how to
plot curves in the ipython notebook

# Warmup (to do during the lab sections)

Let set up the notebook to display plots inline instead of lauching a separate
plot viewer and let's import the modules we will need throughout this homework:


    import matplotlib
    %matplotlib inline

###Exercice 1. *Fill lists with function values.*
Write a Python functin representing the mathatematical function
$$h(x)=\frac1{\sqrt{2\pi}}e^{-\frac12x^2}.$$


    def hx(x):
        from math import exp,sqrt,pi
        return exp(-1/2*x**2)*1/sqrt(2*pi)
    print hx(0)

    0.398942280401


In the cell below, define the lists <code>xlist</code> and <code>hlist</code>
and populate them with $x$ and $h(x)$ values for 41 uniformly spaced $x$
coordinates in $[−4,4]$. Use list comprenhension to do that.


    import numpy as np
    xlist=np.arange(-4.0,4.1,0.2)
    #len(xlist)
    hlist=[]
    for xl in xlist:
        hlist.append(hx(xl))
        

Use the lists you defined above to plot the function $h(x)$ in the interval
$[-4,4]$. Label the x axis by "x" and the y-axis by "h(x)" and give as title for
your plot "The graph of the Gausian".

Use the matplotlib object-oriented API as described in the notebook in the
reading assignement.


    import matplotlib.pyplot as plt
    from pylab import *
    figure()
    plot(xlist,hlist,"r")
    xlabel("x")
    ylabel("h(x)")
    title("The graph of the Gausian")
    show()


![png](https://raw.githubusercontent.com/hrwang/PythonHW/master/HW5_10_0.png)


Redo the same exercise using now Numpy arrays, Numpy <code>linspace</code>
function, and vectorization, instead of lists and list comprehension in the cell
below.


    xlist_array=linspace(-4,4,41)
    hlist_array=array(hlist)
    figure()
    plot(xlist_array,hlist_array,"r")
    xlabel("x")
    ylabel("h(x)")
    title("The graph of the Gausian")
    show()


![png](https://raw.githubusercontent.com/hrwang/PythonHW/master/HW5_12_0.png)


# Graded Exercises

###Exercise 2. *Apply a function to a vector.*
Given a vector $v = (2,3,−1)$ and a function $f(x) = x^3 + xe^x + 1$,
apply $f$ to each element in $v$ and store the results in the list $w$ using
list comprehension.

Then calculate $f(v)$ as $v^3 +ve^v +1$ using Numpy arrays and vector computing
rules. Store result in the variable $z$.

Print the difference between the two vectors $w$ and $z$ and make sure its
entries are zero.


    def fx(x):
        from math import exp
        return x**3+x*exp(x)+1
    v=(2,3,-1)
    w=[]
    for a in v:
        w.append(fx(a))
    #print w
    
    V=np.array(v)
    z=np.array([fx(a) for a in V])
    print z-w

    [ 0.  0.  0.]


###Exercise 3. *Matrix manipulations*


Consider the following matrices:


$$
A = \left(\begin{array}{ccc}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{array}\right)\qquad
B = \left(\begin{array}{ccc}
0 & 2 & 0 & 4 \\
4 & 0 & 1 & 2\\
6 & 8 & 3 & 1\\
\end{array}\right)\qquad
C = \left(\begin{array}{ccc}
10 & 24 & 8 \\
14 & 54 & 16 \\
\end{array}\right)
$$


and column and row vectors


$$
v = \left(\begin{array}{ccc}
10  \\
4  \\
73  \\
\end{array}\right)\qquad
w = \left(\begin{array}{ccc}
5 & 8 & 9  \\
\end{array}\right)\qquad
$$

In the cell below, store the matrices in the variables a, b, and c as list of
lists, and the vectors in the variables v and w, also as list of lists.

**Caution:** $v$ is a column vector, while $w$ is a row vector.


    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[[0,2,0,4],[4,0,1,2],[6,8,3,1]]
    c=[[10,24,8],[14,54,16]]
    v=[[10],[4],[73]]
    w=[5,8,9]
    NNL='\n\n'
    print a,NNL,b,NNL,c,NNL,v,NNL,w

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    
    [[0, 2, 0, 4], [4, 0, 1, 2], [6, 8, 3, 1]] 
    
    [[10, 24, 8], [14, 54, 16]] 
    
    [[10], [4], [73]] 
    
    [5, 8, 9]


In the cell below, convert the vectors and matrices above into numpy arrays and
store these objects in the variables A, B, C, V, and W.

Then print these variables (check that you have the right matrices and vectors)
as well as their shapes (you may want to write a for loop):


    content_ls=[a,b,c,v,w]
    #print np.array(a)
    A=np.array(a)
    B=np.array(b)
    C=np.array(c)
    V=np.array(v)
    W=np.array(w)
    content_arr=[A,B,C,V,W]
    NL='\n'
    name_arr=['A','B','C','V','W']
    for x,y,z in zip(content_ls,name_arr,content_arr):
        #z=np.array(z)
        z=np.array(x)
        print y,"=",NL,z
        
    #print W[2]
    W         ### The global variable can not be modified inside the function?

    A = 
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    B = 
    [[0 2 0 4]
     [4 0 1 2]
     [6 8 3 1]]
    C = 
    [[10 24  8]
     [14 54 16]]
    V = 
    [[10]
     [ 4]
     [73]]
    W = 
    [5 8 9]





    array([5, 8, 9])



Compute the the sine of $A, B, C, V$ and $W$ and print the result (use a for
loop):


    for x,y in zip (name_arr,content_arr):
        print "sin",x,"=",NL,np.sin(y)
        


    sin A = 
    [[ 0.84147098  0.90929743  0.14112001]
     [-0.7568025  -0.95892427 -0.2794155 ]
     [ 0.6569866   0.98935825  0.41211849]]
    sin B = 
    [[ 0.          0.90929743  0.         -0.7568025 ]
     [-0.7568025   0.          0.84147098  0.90929743]
     [-0.2794155   0.98935825  0.14112001  0.84147098]]
    sin C = 
    [[-0.54402111 -0.90557836  0.98935825]
     [ 0.99060736 -0.55878905 -0.28790332]]
    sin V = 
    [[-0.54402111]
     [-0.7568025 ]
     [-0.67677196]]
    sin W = 
    [-0.95892427  0.98935825  0.41211849]


Convert the arrays A, B, C, V, and W into numpy matrices and store them in the
variables AA, BB, CC, VV, and WW:


    AA=np.matrix(A)
    BB=np.matrix(B)
    CC=np.matrix(C)
    VV=np.matrix(V)
    WW=np.matrix(W)

Compute the following matrix products and additions:

1. $\operatorname{I} + A + \frac1{2}A^2 + \frac1{6}A^3$
1. $Av$, $wB$, $v^TB$, $v^TC^T$, and $v^T$

where $\operatorname{I}$ is the identity matrix, and print the result:


    print np.eye(3,3)+A+A*A*1/2.0+A**3*1/6.0,NL
    print np.eye(3,3)+AA+AA*AA*1/2.0+AA**3*1/6.0,NL
    print AA*v,NL
    print w*BB,NL
    print V.transpose()*BB,NL
    #1/2.0*2
    #A*A
    #np.eye(3,3)+AA+AA*AA*1/2

    [[   2.66666667    5.33333333   12.        ]
     [  22.66666667   39.33333333   60.        ]
     [  88.66666667  125.33333333  172.        ]] 
    
    [[  95.  116.  138.]
     [ 214.  264.  312.]
     [ 334.  410.  487.]] 
    
    [[237]
     [498]
     [759]] 
    
    [[86 82 35 45]] 
    
    [[454 604 223 121]] 
    


###Exercise 4. * A wave class with plotting capabilities. *
The collection of functions

$$f(x,t; a)=e^{−a(x−3t)^2} \sin(3\pi(x−t))$$

describes a wave localized in space ($x$ variable) at time $t$, where $a$ is a
parameter.

Write a class <code>Wave</code> representing this family of functions satisfying
the following specifications:

The constructor should be of the form

    def __init__(self, a=1, interval=[-4, 4], pt_num=40):
where $a$ is the parameter,  <code>interval</code> is a list consisting of the
lower-bound and the upper-bound for the $x$-variable, and <code>pt_num</code> is
the number of points to be sampled for the $x$ variable when plotting. The
constructor should store the values passed to it in the class attributes:

        self.a = a
        self.x0 = interval[0]
        self.x1 = interval[1]
        self.pt_num = pt_num

You should implement the following methods:

    def compute(self, x,t):
that should return the value $f(x,t;a)$ with parameter $a$ having the value
stored in the attribute <code>self.a</code>.

    def x_values(self):
that should return a numpy array of <code>self.pt_num</code> points between
<code>self.x0</code> and
<code>self.x1</code>

    def plot(self, time):
that should draw four plots of the function $f$ arranged in a ROW (use the
<code>subplots</code> method) at different times (equally spaced between $0$ and
<code>time</code>. The $x$-axis should be labelled 'x' and the $y$-axis should
be labelled 'y'. The title of each of the plot should indicate the time at which
the wave is plotted.



    class wave:
        def __init__(self, a=1, interval=[-4, 4], pt_num=40):
            self.a=a
            self.x0=interval[0]
            self.x1=interval[1]
            self.pt_num=pt_num
        def compute (self,x,t):
            from math import exp,pi
            from numpy import sin
            A=exp(-self.a*(x-3*t)**2)
            B=sin(3*pi*(x-t))
            return A*B
        def x_values(self):
            import numpy
            return linspace(self.x0,self.x1,self.pt_num)
        def plot(self,time=4):
            import numpy
            import matplotlib.pyplot as plt
            %matplotlib inline
            values=self.x_values()
            t_values=linspace(0,time,4)
            fig,axes=plt.subplots(nrows=1,ncols=4,figsize=(18,4))
            for t_value,ax in zip(t_values,axes):
                y_values=[]
                for x_value in values:
                    y_value=self.compute(x_value,t_value)
                    y_values.append(y_value)
                y_values=numpy.array(y_values)
                ax.plot(values, y_values, 'r')
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_title("t=" + str(t_value))
            fig.tight_layout()

Test the class by executing the following cell (you can play with the interval
and the parameter $a$):


    a=2
    interval=[-1,1]
    F=wave(a,interval)
    F.plot(1)


![png](https://raw.githubusercontent.com/hrwang/PythonHW/master/HW5_30_0.png)



    
