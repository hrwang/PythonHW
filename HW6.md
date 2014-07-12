
### Discussions:
1. Series acess: a[10] and a [10:11]. One acesses by index, the other by the
number of rows.
2. "=" in list does not creat new object, it is just a pointer. but in pandas
series, it creats new object.

# Stat 133: Homework 6

## Deadline: October 19, 4 a.m.

This week homework concerns the most important module and classes you'll learn
for data analysis in Python:

* the Pandas module, which defines
* the <code>Series</code> class and the <code>DataFrame</code> classes

These two last classes will come up in a very similar guise, when we start R
after the midterm. So do your best to get them down.

##Reading assignment

The Monday quiz questions will be taken from the following reading assignment:

* [10 minutes to Pandas](http://pandas.pydata.org/pandas-docs/dev/10min.html)

Here are some further readings (that do not concern Monday's quiz), where you
can find information on the Pandas module to help you with this week homework:

* The ipython notebook tutorial [learn Pandas](https://bitbucket.org/hrojas
/learn-pandas)
* [Python for Data Analysis](http://proquest.safaribooksonline.com/book/programm
ing/python/9781449323592), which should become from now on your book of
reference ;)

From "Python for Data Analysis," I suggest that you read:

* Section 5: [Getting started with Panda](http://proquest.safaribooksonline.com/
book/programming/python/9781449323592/5dot-getting-started-with-
pandas/id2828260),
and within that section, the paragraph:
[Summarizing and Computing Descriptive Statistics](http://proquest.safaribookson
line.com/book/programming/python/9781449323592/5dot-getting-started-with-pandas/
id2828260#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE0NDkzMjM1OTIlMkZpZDI4MzA4ODMmcX
Vlcnk9)


* within Section 8, the paragraph: [Plotting Functions in Pandas](http://proques
t.safaribooksonline.com/book/programming/python/9781449323592/5dot-getting-
started-with-pandas/id2828260#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE0NDkzMjM1OT
IlMkZpZDI4MDIyMDgmcXVlcnk9)







# Warmup (to do during the lab sections)

Let's import the Pandas module as pd and its two main classes
<code>DataFrame</code> and <code>Serie</code> directly.

We will also need the function <code>randrange</code> from the
<random>module</random>.

Also write the magic command to have the plots inline in the ipython notebook.


    import pandas as pd
    import numpy as np
    import matplotlib
    %matplotlib inline

    /Library/Python/2.7/site-packages/pandas/io/excel.py:626: UserWarning: Installed openpyxl is not supported at this time. Use >=1.6.1 and <2.0.0.
      .format(openpyxl_compat.start_ver, openpyxl_compat.stop_ver))


Now generate three dictionaries

    final_grades
    midterm_grades
    homework_grades

with keys being randomly generated student names, and values being randomly
generated student grades from 0 to 100.


    from random import randint
    randint(0,101)
    grades=np.random.randint(50,100,12).reshape(4,3)
    grades[1]
    final_grades={'ming':grades[0,0], \
                  'jun':grades[1,0], \
                  'hua':grades[2,0], \
                  'qing':grades[3,0]
                  }
    midterm_grades={'ming':grades[0,1], \
                  'jun':grades[1,1], \
                  'hua':grades[2,1], \
                  'qing':grades[3,1]
                  }
    homework_grades={'ming':grades[0,2], \
                  'jun':grades[1,2], \
                  'hua':grades[2,2], \
                  'qing':grades[3,2]
                  }
    homework_grades




    {'hua': 58, 'jun': 50, 'ming': 95, 'qing': 88}



Create three Pandas Series from the dictionary above:

* The dictionary F contains the grades for the final exam, has name "Final", and
dtype float
* The dictionary M contains the grades for the midterm exam, has name "Midterm",
and dtype float
* The dictionary H contains the grades for the homework exam, has name
"Homework", and dtype float


    F=pd.Series(final_grades.values(),dtype=float)
    M=pd.Series(midterm_grades.values(),dtype=float)
    H=pd.Series(homework_grades.values(),dtype=float)

In three different cells, print the histogram of the grades contained in the
Series F, M, and H, and then display their first:


    F=pd.Series(np.random.randint(60,100,100))
    F.hist(color='coral',bins=16)
    print (F[1])

    84



![png](https://raw.githubusercontent.com/hrwang/PythonHW/master/HW6_13_1.png)



    


    

# Graded Exercises

## Exercise 1

Create a Pandas DataFrame object containing the three series F, M, and H above
as columns, and print it the first 20 lines with the method <code>head</code>:


    F=pd.Series(np.random.randint(60,100,100))
    M=pd.Series(np.random.randint(30,80,100))
    H=pd.Series(np.random.randint(80,100,100))
    dF=pd.DataFrame(F,columns=['final'])
    dM=pd.DataFrame(M,columns=['midterm'])
    dH=pd.DataFrame(H,columns=['homework'])
    
    dgrades=pd.concat([dF,dM,dH],axis=1)
    dgrades.head(20)





<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>final</th>
      <th>midterm</th>
      <th>homework</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 </th>
      <td> 63</td>
      <td> 42</td>
      <td> 84</td>
    </tr>
    <tr>
      <th>1 </th>
      <td> 85</td>
      <td> 45</td>
      <td> 96</td>
    </tr>
    <tr>
      <th>2 </th>
      <td> 88</td>
      <td> 30</td>
      <td> 80</td>
    </tr>
    <tr>
      <th>3 </th>
      <td> 61</td>
      <td> 40</td>
      <td> 82</td>
    </tr>
    <tr>
      <th>4 </th>
      <td> 62</td>
      <td> 57</td>
      <td> 93</td>
    </tr>
    <tr>
      <th>5 </th>
      <td> 71</td>
      <td> 69</td>
      <td> 92</td>
    </tr>
    <tr>
      <th>6 </th>
      <td> 90</td>
      <td> 45</td>
      <td> 87</td>
    </tr>
    <tr>
      <th>7 </th>
      <td> 82</td>
      <td> 47</td>
      <td> 99</td>
    </tr>
    <tr>
      <th>8 </th>
      <td> 74</td>
      <td> 40</td>
      <td> 88</td>
    </tr>
    <tr>
      <th>9 </th>
      <td> 63</td>
      <td> 57</td>
      <td> 87</td>
    </tr>
    <tr>
      <th>10</th>
      <td> 69</td>
      <td> 46</td>
      <td> 81</td>
    </tr>
    <tr>
      <th>11</th>
      <td> 91</td>
      <td> 50</td>
      <td> 84</td>
    </tr>
    <tr>
      <th>12</th>
      <td> 66</td>
      <td> 74</td>
      <td> 99</td>
    </tr>
    <tr>
      <th>13</th>
      <td> 61</td>
      <td> 39</td>
      <td> 91</td>
    </tr>
    <tr>
      <th>14</th>
      <td> 69</td>
      <td> 74</td>
      <td> 82</td>
    </tr>
    <tr>
      <th>15</th>
      <td> 71</td>
      <td> 62</td>
      <td> 85</td>
    </tr>
    <tr>
      <th>16</th>
      <td> 79</td>
      <td> 52</td>
      <td> 85</td>
    </tr>
    <tr>
      <th>17</th>
      <td> 95</td>
      <td> 31</td>
      <td> 91</td>
    </tr>
    <tr>
      <th>18</th>
      <td> 69</td>
      <td> 33</td>
      <td> 91</td>
    </tr>
    <tr>
      <th>19</th>
      <td> 96</td>
      <td> 57</td>
      <td> 82</td>
    </tr>
  </tbody>
</table>
</div>



Compute the total grades for the class knowing that the total grade is split
into

* 50% for the final exam, 40% for the midterm, and 10% for the homework grade.

Store the result in a Series named

    total_grades

Then display the histogram of this Series, as well as its histogram


    total_grades=dgrades['final']*.5+dgrades['midterm']*.4+.1*dgrades['homework']
    total_grades.hist(bins=20,color='forestgreen')




    <matplotlib.axes.AxesSubplot at 0x10950ba90>




![png](https://raw.githubusercontent.com/hrwang/PythonHW/master/HW6_21_1.png)


Add the <code>total_grade</code> Series you created above to the
<code>GRADES</code> DataFrame, as a column named "Total" .

Print the first 20 entries of the GRADE DataFrame, and display the histogram of
the different grades it contains:


    d_total=pd.DataFrame(total_grades,columns=['Total'])
    dgrades=pd.concat([dgrades,d_total],axis=1)
    dgrades.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>final</th>
      <th>midterm</th>
      <th>homework</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 63</td>
      <td> 42</td>
      <td> 84</td>
      <td> 56.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 85</td>
      <td> 45</td>
      <td> 96</td>
      <td> 70.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 88</td>
      <td> 30</td>
      <td> 80</td>
      <td> 64.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 61</td>
      <td> 40</td>
      <td> 82</td>
      <td> 54.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 62</td>
      <td> 57</td>
      <td> 93</td>
      <td> 63.1</td>
    </tr>
  </tbody>
</table>
</div>



## Exercise 2

This exercise goal is to get you used to define on your own the steps to be
executed to carry out a project in data anlysis.  You will need to define what
needs to be accomplished and look up in the reading assignments above (or on
google) how to carry out this steps out.

This exercise is a simple preparation to the class project.

Using Python, you'll have to retrieve the CSV (Comma Separated Values) file at
the address:

https://dl.dropboxusercontent.com/u/48599099/Stat133/data/ALL_GRADES.csv

To give you an idea of what the file is about, I'll do this in bash below (but
you'll have to download the file in Python by yourself).


    ### Download the data, read them into pandas dataframe object:
    url='https://dl.dropboxusercontent.com/u/48599099/Stat133/data/ALL_GRADES.csv'
    all_grades=pd.read_csv(url,)
    all_grades.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student</th>
      <th>F</th>
      <th>HW1</th>
      <th>HW2</th>
      <th>HW3</th>
      <th>HW4</th>
      <th>HW5</th>
      <th>HW6</th>
      <th>HW7</th>
      <th>HW8</th>
      <th>HW9</th>
      <th>HW10</th>
      <th>HW11</th>
      <th>THW</th>
      <th>M1</th>
      <th>M2</th>
      <th>TG</th>
      <th>LG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 0108_Student</td>
      <td> 10.5</td>
      <td> 10</td>
      <td> 9</td>
      <td>  9</td>
      <td> 10</td>
      <td> 10</td>
      <td>  4</td>
      <td> 10</td>
      <td>  6</td>
      <td>  9</td>
      <td>  0</td>
      <td>  7</td>
      <td>  8.88</td>
      <td>  8</td>
      <td>  9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 0154_Student</td>
      <td> 16.0</td>
      <td> 10</td>
      <td> 9</td>
      <td>  9</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10.00</td>
      <td>  9</td>
      <td>  8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 0161_Student</td>
      <td> 13.5</td>
      <td>  8</td>
      <td> 9</td>
      <td>  8</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td>  9</td>
      <td> 10</td>
      <td>  9</td>
      <td>  9.66</td>
      <td> 10</td>
      <td>  9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 0233_Student</td>
      <td> 14.5</td>
      <td> 10</td>
      <td> 8</td>
      <td> 10</td>
      <td> 10</td>
      <td>  8</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 15</td>
      <td> 10</td>
      <td> 10.56</td>
      <td>  9</td>
      <td>  8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 0310_Student</td>
      <td> 20.0</td>
      <td> 10</td>
      <td> 9</td>
      <td>  8</td>
      <td>  8</td>
      <td> 10</td>
      <td>  8</td>
      <td> 10</td>
      <td> 10</td>
      <td>  9</td>
      <td> 10</td>
      <td>  6</td>
      <td>  9.33</td>
      <td>  8</td>
      <td> 10</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



The file you downloaded contains all grades for a certain class. The table
header

    Student,F,HW1,HW2,HW3,HW4,HW5,HW6,HW7,HW8,HW9,HW10,HW11,THW,M1,M2,TG,LG

gives the column names:

    F   = Final exam
    HWi = Homework number i
    THW = Total homework grade
    M1  = Midterm I
    M2  = Midterm II
    TG  = Total point grade
    LG  = Letter Grade

The last two columns are empty. Your goal is to compute the total grade and the
corresponding letter grade for each student and add this column to the file, (so
that you can upload it on bearfacts for your class for instance). The file you
end up with should be of the exam same format as the file you downloaded from
the internet, except with the columns TG and LG filled up.

The constraint is the following:

1. You need to use the Pandas module

1. You need to compute total point grade for each student with the formula
knowing that the total grade splits into 30% final grade, 25% each midterm, and
20% for the total homework grade


1. Once computed, you need to plot the histogram of total point grades (TG)

1. You need to assign each student a letter-grade between A, B, C, D, and F
(there is no + or - letter grade in this class) with the constraint that, at the
end,

    * 30% of the students get a A
    * 30% of the students get a B
    * 20% of the students get a C
    * 10% of the students get a D
    * 10% of the students get a F

1. Then you need to upadate the grade file correctly with your computed total
grade and letter grades

**Create as many code cells as you want, but detail your computations in
markdown cells surrounding them.**




    ### caluculate the total grades and make serval dataframe copy for the following use:
    tgo=all_grades['F']*.3+all_grades['M1']*.25+all_grades['M2']*.25+all_grades['THW']*.20
    tgo.hist(color='royalblue')
    tgs=tgo              ####  creat a copy, creates new object.
    tgss=tgo             #### creat another copy.
    tg=tgo.tolist()   


![png](https://raw.githubusercontent.com/hrwang/PythonHW/master/HW6_29_0.png)



    ### caluculate how many student will get ABCDF respectively:
    
    a_cut=int(len(tg)*.3)
    b_cut=int(len(tg)*(.3+.3))
    c_cut=int(len(tg)*(.3+.3+.2))
    d_cut=int(len(tg)*(.3+.3+.2+.1))
    
    tg.sort(reverse=True)


    ### Get the boundries for determining LG:
    
    a=tg[a_cut:a_cut+1]
    b=tg[b_cut:b_cut+1]
    c=tg[c_cut:c_cut+1]
    d=tg[d_cut:d_cut+1]


    ### Determine LG for each student:
    lg=[]
    for i in tgss.tolist():
        if i>=a:
            lg.append("A")
        elif i>=b[0]:
            lg.append("B")
        elif i>=c[0]:
            lg.append("C")
        elif i>=d[0]:
            lg.append("D")
        else:
            lg.append("F")


    ### Make new dataframe:
    
    lgs=pd.Series(lg)
    df_test=pd.concat([tgs,lgs],axis=1)
    df=df_test.rename(columns={1:'LG',0:'TG'})
    df_test=all_grades.iloc[:,:16]
    allgrade_final=pd.concat([df_test,df],axis=1)
    allgrade_final["TG"] = allgrade_final.TG.map("{0:.2f}".format)    ### format the score, with two digits after the decimal points.
    allgrade_final.to_csv('all_grades.csv')
    allgrade_final.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student</th>
      <th>F</th>
      <th>HW1</th>
      <th>HW2</th>
      <th>HW3</th>
      <th>HW4</th>
      <th>HW5</th>
      <th>HW6</th>
      <th>HW7</th>
      <th>HW8</th>
      <th>HW9</th>
      <th>HW10</th>
      <th>HW11</th>
      <th>THW</th>
      <th>M1</th>
      <th>M2</th>
      <th>TG</th>
      <th>LG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 0108_Student</td>
      <td> 10.5</td>
      <td> 10</td>
      <td> 9</td>
      <td>  9</td>
      <td> 10</td>
      <td> 10</td>
      <td>  4</td>
      <td> 10</td>
      <td>  6</td>
      <td>  9</td>
      <td>  0</td>
      <td>  7</td>
      <td>  8.88</td>
      <td>  8</td>
      <td>  9</td>
      <td>  9.18</td>
      <td> B</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 0154_Student</td>
      <td> 16.0</td>
      <td> 10</td>
      <td> 9</td>
      <td>  9</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10.00</td>
      <td>  9</td>
      <td>  8</td>
      <td> 11.05</td>
      <td> A</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 0161_Student</td>
      <td> 13.5</td>
      <td>  8</td>
      <td> 9</td>
      <td>  8</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td>  9</td>
      <td> 10</td>
      <td>  9</td>
      <td>  9.66</td>
      <td> 10</td>
      <td>  9</td>
      <td> 10.73</td>
      <td> A</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 0233_Student</td>
      <td> 14.5</td>
      <td> 10</td>
      <td> 8</td>
      <td> 10</td>
      <td> 10</td>
      <td>  8</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 10</td>
      <td> 15</td>
      <td> 10</td>
      <td> 10.56</td>
      <td>  9</td>
      <td>  8</td>
      <td> 10.71</td>
      <td> A</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 0310_Student</td>
      <td> 20.0</td>
      <td> 10</td>
      <td> 9</td>
      <td>  8</td>
      <td>  8</td>
      <td> 10</td>
      <td>  8</td>
      <td> 10</td>
      <td> 10</td>
      <td>  9</td>
      <td> 10</td>
      <td>  6</td>
      <td>  9.33</td>
      <td>  8</td>
      <td> 10</td>
      <td> 12.37</td>
      <td> A</td>
    </tr>
  </tbody>
</table>
</div>




    


    
