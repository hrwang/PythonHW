
# Stat 133: Homework 8 (Deadline: November 2, 4 a.m.)

# Data Analysis using DataFrames

# Warmup (to do during the lab sections)

1. Dataframe(data,columns=['S']) does not work, why?
2. index_col=0, make the boxplot does not work. No, it works. So the second row
does not affect the real data structure of the object dataframe. One point that
is diff from R dataframe.
3. Boxplot catagorical data?


    from pandas import DataFrame, Series
    import pandas as pd

    /Library/Python/2.7/site-packages/pandas/io/excel.py:626: UserWarning: Installed openpyxl is not supported at this time. Use >=1.6.1 and <2.0.0.
      .format(openpyxl_compat.start_ver, openpyxl_compat.stop_ver))


The data we are going to analyse in this homework comes from the grades of a
large class. Let's have a quick look at it:


    url = 'https://dl.dropboxusercontent.com/u/48599099/Stat133/grade_data/CLEANNED/GRADES.csv'
    !curl $url 2>/dev/null | head -3

    SID,M1,M2,FIN,MAJOR,SECTION,HW1,HW2,HW3,HW4,HW5,HW6,HW7,HW8,HW9,HW10,HW11
    40840981,10.0,7.0,16.7,EECS,DS1,8.0,8.0,6.0,7.0,7.0,6.0,9.0,9.0,8.0,14.0,10.0
    41401613,10.0,6.0,15.2,MATH,DS2,8.0,7.0,9.0,9.0,6.0,0.0,0.0,0.0,0.0,0.0,0.0



    

Let's load this csv table into a DataFrame, setting the first column to be the
DataFrame index.

Call this DataFrame <code>data</code>.


    data = pd.read_csv(url,index_col=0)
    data.head()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
      <th>MAJOR</th>
      <th>SECTION</th>
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
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40840981</th>
      <td> 10</td>
      <td> 7</td>
      <td> 16.7</td>
      <td> EECS</td>
      <td> DS1</td>
      <td>  8.00</td>
      <td> 8</td>
      <td> 6</td>
      <td> 7</td>
      <td>  7</td>
      <td> 6</td>
      <td>  9</td>
      <td> 9</td>
      <td> 8</td>
      <td> 14</td>
      <td> 10</td>
    </tr>
    <tr>
      <th>41401613</th>
      <td> 10</td>
      <td> 6</td>
      <td> 15.2</td>
      <td> MATH</td>
      <td> DS2</td>
      <td>  8.00</td>
      <td> 7</td>
      <td> 9</td>
      <td> 9</td>
      <td>  6</td>
      <td> 0</td>
      <td>  0</td>
      <td> 0</td>
      <td> 0</td>
      <td>  0</td>
      <td>  0</td>
    </tr>
    <tr>
      <th>41734527</th>
      <td>  2</td>
      <td> 5</td>
      <td>  8.4</td>
      <td> MATH</td>
      <td> DS0</td>
      <td>  9.75</td>
      <td> 9</td>
      <td> 6</td>
      <td> 9</td>
      <td>  8</td>
      <td> 5</td>
      <td>  9</td>
      <td> 6</td>
      <td> 0</td>
      <td>  9</td>
      <td>  1</td>
    </tr>
    <tr>
      <th>41886821</th>
      <td>  0</td>
      <td> 5</td>
      <td> 11.5</td>
      <td> EECS</td>
      <td> DS0</td>
      <td> 10.00</td>
      <td> 9</td>
      <td> 7</td>
      <td> 8</td>
      <td>  8</td>
      <td> 5</td>
      <td>  8</td>
      <td> 4</td>
      <td> 4</td>
      <td> 10</td>
      <td>  0</td>
    </tr>
    <tr>
      <th>41935225</th>
      <td>  8</td>
      <td> 6</td>
      <td> 10.5</td>
      <td> BIOL</td>
      <td> DS7</td>
      <td> 10.00</td>
      <td> 9</td>
      <td> 8</td>
      <td> 8</td>
      <td> 10</td>
      <td> 4</td>
      <td> 10</td>
      <td> 8</td>
      <td> 0</td>
      <td>  8</td>
      <td>  0</td>
    </tr>
  </tbody>
</table>
</div>



## Exercise 1: Analysis of the exam grades

* Create a DataFrame <code>exams</code> with three columns corresponding to the
final exam grades, and the first and second midterm grades.

* You should rescale the grades so that they are all over 100 points.

* Then print the first entries of this DataFrame

**Remark:** The final is over 20 points, while the midterms are over 10 points.


    score_three=pd.concat([data.M1*10,data.M2*10,data.FIN*5],axis=1)
    score_three[1:2]




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>41401613</th>
      <td> 100</td>
      <td> 60</td>
      <td> 76</td>
    </tr>
  </tbody>
</table>
</div>



* Print the sumary statistics of the exam grades:


    score_three.describe()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td> 249.000000</td>
      <td> 249.000000</td>
      <td> 249.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>  67.911647</td>
      <td>  64.698795</td>
      <td>  59.018072</td>
    </tr>
    <tr>
      <th>std</th>
      <td>  28.772891</td>
      <td>  27.620879</td>
      <td>  24.519427</td>
    </tr>
    <tr>
      <th>min</th>
      <td>   0.000000</td>
      <td>   0.000000</td>
      <td>   0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>  50.000000</td>
      <td>  50.000000</td>
      <td>  46.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>  70.000000</td>
      <td>  70.000000</td>
      <td>  63.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>  90.000000</td>
      <td>  90.000000</td>
      <td>  77.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td> 100.000000</td>
      <td> 100.000000</td>
      <td> 102.500000</td>
    </tr>
  </tbody>
</table>
</div>



* Give the definition of these **summary statistics** in the markdown cell below
(use google if necessary):

###Definitions:
* count: number of data points
* mean:  average
* std:   standard deviaton
* min:   minimum number in this dataset
* 25% (1st quartile):
* 50% (median):
* 75% (3rd quartile):
* max:

* Use the <code>boxplot</code> method of DataFrame to visualize these summary
statistics:


    %pylab inline
    score_three.boxplot()

    Populating the interactive namespace from numpy and matplotlib





    {'boxes': [<matplotlib.lines.Line2D at 0x10c5bfc10>,
      <matplotlib.lines.Line2D at 0x10c5c9450>,
      <matplotlib.lines.Line2D at 0x10c5cec50>],
     'caps': [<matplotlib.lines.Line2D at 0x10c5bf210>,
      <matplotlib.lines.Line2D at 0x10c5bf710>,
      <matplotlib.lines.Line2D at 0x10c5c6a10>,
      <matplotlib.lines.Line2D at 0x10c5c6f10>,
      <matplotlib.lines.Line2D at 0x10c5ce250>,
      <matplotlib.lines.Line2D at 0x10c5ce750>],
     'fliers': [<matplotlib.lines.Line2D at 0x10c5c3650>,
      <matplotlib.lines.Line2D at 0x10c5c3b10>,
      <matplotlib.lines.Line2D at 0x10c5c9e50>,
      <matplotlib.lines.Line2D at 0x10c5cc350>,
      <matplotlib.lines.Line2D at 0x10c5d1690>,
      <matplotlib.lines.Line2D at 0x10c5d1b50>],
     'medians': [<matplotlib.lines.Line2D at 0x10c5c3150>,
      <matplotlib.lines.Line2D at 0x10c5c9950>,
      <matplotlib.lines.Line2D at 0x10c5d1190>],
     'whiskers': [<matplotlib.lines.Line2D at 0x10c5bc6d0>,
      <matplotlib.lines.Line2D at 0x10c5bccd0>,
      <matplotlib.lines.Line2D at 0x10c5c3fd0>,
      <matplotlib.lines.Line2D at 0x10c5c6510>,
      <matplotlib.lines.Line2D at 0x10c5cc810>,
      <matplotlib.lines.Line2D at 0x10c5ccd10>]}




![png](HW8_files/HW8_18_2.png)


The <code>boxplot</code> method makes a **box** (the rectangle in blue) and
**whisker** plot (the vertical dashed line in black steming from the blue box)
summarizing a squence of data points.

The box extends from the 1st quartile of the data $Q_1$ (with a (read) line at
the median $Q_2$) to the 3rd quartile of the data $Q_3$.

The whiskers extend from the box to an horizontal segment, representing the end
of the whiskers:

* The lower whisker is located at the value $Q_1 - 1.5(Q_3 - Q_1)$
* The upper whisker is located at the value $Q_3 + 1.5(Q_3 - Q_1)$

Data points past the lower and upper whiskers are called **outliers**. These are
exceptional values that somehow fall outide the standard population behavior.

## Exercise 2. Analysis of the exam grades grouped by majors

We would like to see if there is a difference in student performance for
different majors in the final exam.

Let's first try to understand the repartition of majors in the class.

* Use the Series method <code>Series.value_count(normalize=False)</code> to
obtain a series representing the distribution of majors in the class. Store this
series in a variable called <code>major_dist</code>, and print it.

Setting the method argument to <code>normalize=True</code> will give you class
percentage per major, instead of the number of students per major.


    data.head()
    #x=Series(data.MAJOR)
    #x.value_counts()
    data.MAJOR.value_counts(normalize=True)




    DOUB    0.269076
    MATH    0.204819
    EECS    0.160643
    PHYS    0.076305
    ECON    0.060241
    STAT    0.056225
    BIOL    0.036145
    dtype: float64



* Plot the <code>major_dist</code> Series as an horizontal **bar plot** instead
of a **line** plot, by setting the <code>plot</code> argument **kind** to the
value **barh**.


    data.MAJOR.value_counts(normalize=True).plot(kind='barh')




    <matplotlib.axes.AxesSubplot at 0x10c76b6d0>




![png](HW8_files/HW8_24_1.png)


* Construct a DataFrame named <code>average</code> with a single column named
"mean" from the DataFrame <code>exams</code> by averaging on the rows (i.e. by
computing the average grade per student), and display the first entries of the
DataFrame:


    score_three['average']=(score_three.FIN+score_three.M1+score_three.M2)/3
    score_three.head(1)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
      <th>average</th>
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40840981</th>
      <td> 100</td>
      <td> 70</td>
      <td> 83.5</td>
      <td> 84.5</td>
    </tr>
  </tbody>
</table>
</div>



* Add to the DataFrame <code>average</code> the column "MAJOR" from the
DataFrame <code>data</code> using the bracket notation, then display its first
entries:


    score_three['major']=data.MAJOR
    score_three.head(1)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
      <th>average</th>
      <th>major</th>
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40840981</th>
      <td> 100</td>
      <td> 70</td>
      <td> 83.5</td>
      <td> 84.5</td>
      <td> EECS</td>
    </tr>
  </tbody>
</table>
</div>



* Using the DataFrame method <code> DataFrame.boxplot(by) </code>, display the
boxplots of the average per major, by setting the "by" argment to the column
"MAJOR":


    score_three.boxplot(column='average',by=['major'])




    <matplotlib.axes.AxesSubplot at 0x10c806690>




![png](HW8_files/HW8_30_1.png)


* Explain in the markdown cell below what you see from the boxplot above if
anything.

**Explanation:** for you to complete

# Graded Exercises

## Exercise 3 (Computation the total point grade)

Using the data stored in the DataFrame <code>data</code>, compute the total
point grade for the class.

* Start by computing the homework grade for each student and store the result
back in the DataFrame <code>data</code> as the column 'HW'using the **bracket
operator** (i.e., <code>data['HW'] = ...</code>):


    data.head(3)
    score_three['HW']=(data.HW1+data.HW2+data.HW3+data.HW4+data.HW5+data.HW6+data.HW7+data.HW8+data.HW9+data.HW10+data.HW11)*10/12
    score_three.head(3)
    #max(score_three.HW)
    score_three['PG']=score_three.M1*.2+score_three.M2*.2+score_three.FIN*.4+score_three.HW*.2
    score_three.head(3)
    max(score_three.PG)
    score_three[score_three.PG==99]
    #max(data.M2)
    #data[data.M2==10]
    #max(data.FIN)
    score_three.PG[0:1]




    SID
    40840981    82.733333
    Name: PG, dtype: float64



* Compute the total grades for the class knowing that the total grade is split
into 40% for the final exam, 20% for each midterm, and 20% for the homework
grade. Store the result back into <code>data</code> as the column "PG" (Point
Grade) using the bracket operator. Diplay the first entries of the "PG" column
in <code>data</code>:

**CAUTION: DON'T FORGET TO NORMALIZE THE EXAM GRADES OVER 100 POINTS**



    

* Using the method <code>DataFrame.hist(column)</code> on the Series
<code>data.PG</code> display the repartition of the total point grades. Also
print the statistics summary of the total point grades.


    score_three.PG.hist()




    <matplotlib.axes.AxesSubplot at 0x10c6c5690>




![png](HW8_files/HW8_40_1.png)



    score_three.PG.describe()




    count    249.000000
    mean      63.991432
    std       20.529788
    min        0.000000
    25%       54.500000
    50%       64.666667
    75%       80.000000
    max       99.000000
    dtype: float64



* **Comments on the point grade repartition:**

* Display the statistics summary for the total point grades, and draw the
corresponding boxplot:


    a=DataFrame(score_three.PG)
    a.boxplot()




    {'boxes': [<matplotlib.lines.Line2D at 0x10d267ad0>],
     'caps': [<matplotlib.lines.Line2D at 0x10d2670d0>,
      <matplotlib.lines.Line2D at 0x10d2675d0>],
     'fliers': [<matplotlib.lines.Line2D at 0x10d26c510>,
      <matplotlib.lines.Line2D at 0x10d26c9d0>],
     'medians': [<matplotlib.lines.Line2D at 0x10d267fd0>],
     'whiskers': [<matplotlib.lines.Line2D at 0x10d264590>,
      <matplotlib.lines.Line2D at 0x10d264b90>]}




![png](HW8_files/HW8_44_1.png)


* Compute the values for the lower and upper whisker in the boxplot above (see
Exercise 1 for definitions) and print them. Use the method
<code>Series.quantile(q)</code> to obtain the 1st and 3rd quantiles.


    whisker_low=score_three.PG.quantile(.25)-1.5*(score_three.PG.quantile(.75)-score_three.PG.quantile(.25))
    print (whisker_low)
    
    whisker_up=score_three.PG.quantile(.75)+1.5*(score_three.PG.quantile(.75)-score_three.PG.quantile(.25))
    print (whisker_up)
    #?Series.quantile()

    16.25
    118.25


* Using logical ranges to retrieve the point grades, majors, and sections of the
lower outlier sutdents from <code>data</code> and store the result in a
DataFrame, then display it:


    df_low=score_three[score_three.PG<16.5]
    df_low.head()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
      <th>average</th>
      <th>major</th>
      <th>HW</th>
      <th>PG</th>
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>42251947</th>
      <td>  0</td>
      <td>  0</td>
      <td> 0.0</td>
      <td>  0.0</td>
      <td> EECS</td>
      <td>  0.000000</td>
      <td>  0.000000</td>
    </tr>
    <tr>
      <th>43612326</th>
      <td> 20</td>
      <td> 10</td>
      <td> 0.0</td>
      <td> 10.0</td>
      <td> PHYS</td>
      <td> 20.416667</td>
      <td> 10.083333</td>
    </tr>
    <tr>
      <th>43899409</th>
      <td>  0</td>
      <td>  0</td>
      <td> 0.0</td>
      <td>  0.0</td>
      <td>  NaN</td>
      <td> 15.000000</td>
      <td>  3.000000</td>
    </tr>
    <tr>
      <th>43909412</th>
      <td> 20</td>
      <td> 20</td>
      <td> 9.5</td>
      <td> 16.5</td>
      <td> DOUB</td>
      <td> 19.166667</td>
      <td> 15.633333</td>
    </tr>
    <tr>
      <th>44395088</th>
      <td> 60</td>
      <td>  0</td>
      <td> 0.0</td>
      <td> 20.0</td>
      <td>  NaN</td>
      <td> 15.833333</td>
      <td> 15.166667</td>
    </tr>
  </tbody>
</table>
</div>



## Exercise 2 (Computation of the letter grade)

### Bucket, Quantile, and Group Analysis

* Given that we want 20% of A, 30% of B, 30% of C, 10% of D, and 10% of F,
compute the letter grade for each student and enter it back in the DataFrame
<code>data</code> as the 'LG' column. Display the first entries of the two
columns, 'PG' and 'LG', in <code>data</code>, after you added this new column.

Use the pandas function

    pd.qcut(d, q, labels)
where <code>d</code> is a series of data points, <code>d</code> is a list of
acending numbers from 0 to 1 representing the grade quantiles and
<code>labels</code> are the labels (here: letter grades) that you want to label
the data points in each quantile with.

You can directly add what <code>pd.qcut</code> returns to the DataFrame
<code>data</code> as the column "LG".


    q=[0,.1,.2,.5,.8,1]
    labels=['F','D','C','B','A']
    score_three['LG']=pd.qcut(score_three.PG,q,labels)
    score_three.head()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
      <th>average</th>
      <th>major</th>
      <th>HW</th>
      <th>PG</th>
      <th>LG</th>
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40840981</th>
      <td> 100</td>
      <td> 70</td>
      <td> 83.5</td>
      <td> 84.500000</td>
      <td> EECS</td>
      <td> 76.666667</td>
      <td> 82.733333</td>
      <td> B</td>
    </tr>
    <tr>
      <th>41401613</th>
      <td> 100</td>
      <td> 60</td>
      <td> 76.0</td>
      <td> 78.666667</td>
      <td> MATH</td>
      <td> 32.500000</td>
      <td> 68.900000</td>
      <td> B</td>
    </tr>
    <tr>
      <th>41734527</th>
      <td>  20</td>
      <td> 50</td>
      <td> 42.0</td>
      <td> 37.333333</td>
      <td> MATH</td>
      <td> 59.791667</td>
      <td> 42.758333</td>
      <td> D</td>
    </tr>
    <tr>
      <th>41886821</th>
      <td>   0</td>
      <td> 50</td>
      <td> 57.5</td>
      <td> 35.833333</td>
      <td> EECS</td>
      <td> 60.833333</td>
      <td> 45.166667</td>
      <td> D</td>
    </tr>
    <tr>
      <th>41935225</th>
      <td>  80</td>
      <td> 60</td>
      <td> 52.5</td>
      <td> 64.166667</td>
      <td> BIOL</td>
      <td> 62.500000</td>
      <td> 61.500000</td>
      <td> C</td>
    </tr>
  </tbody>
</table>
</div>



* Verify that you have the right proportion of letter grades by using the
<code>value_counts</code> method of the Series class to obtain the proportion of
students per letter grade. Display the Series returned by
<code>value_counts</code>.

**Remark:** Passing the parameter <code>normalize=True</code> to
<code>value_counts</code> will give percentages instead of student numbers.


    pd.value_counts(score_three.LG,normalize=True)




    B    0.297189
    C    0.297189
    A    0.200803
    D    0.104418
    F    0.100402
    dtype: float64




    pd.value_counts(score_three.LG,normalize=True).plot(kind='bar',rot=True)




    <matplotlib.axes.AxesSubplot at 0x10d3fb310>




![png](HW8_files/HW8_55_1.png)


* Display a bar plot of the Series constructed in the cell above:


    

## Exercise 3 Analysis by sections and major. 

In this exercise, we will compute stats for the class grouped by sections and
majors to see if we can detect different trends for different groups. (For
instance, one section can be not working well, or students in a certain major
may not have a background solid enough for the class, etc.)

The first thing is to obtained a group version of the columns of interest in the
DataFrame <code>data</code> containing all the information we have about the
class.

* Using the DataFrame method <code>boxplot</code> and setting its arguments
<code>column</code> and <code>by</code> to approriate values, dispaly a boxplot
of the total letter grade for each of the sections. The plot should be on the
same axes.


    score_three['section']=data.SECTION
    score_three.boxplot(column=['PG'],by=['section'])
    score_three.head()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1</th>
      <th>M2</th>
      <th>FIN</th>
      <th>average</th>
      <th>major</th>
      <th>HW</th>
      <th>PG</th>
      <th>LG</th>
      <th>section</th>
    </tr>
    <tr>
      <th>SID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40840981</th>
      <td> 100</td>
      <td> 70</td>
      <td> 83.5</td>
      <td> 84.500000</td>
      <td> EECS</td>
      <td> 76.666667</td>
      <td> 82.733333</td>
      <td> B</td>
      <td> DS1</td>
    </tr>
    <tr>
      <th>41401613</th>
      <td> 100</td>
      <td> 60</td>
      <td> 76.0</td>
      <td> 78.666667</td>
      <td> MATH</td>
      <td> 32.500000</td>
      <td> 68.900000</td>
      <td> B</td>
      <td> DS2</td>
    </tr>
    <tr>
      <th>41734527</th>
      <td>  20</td>
      <td> 50</td>
      <td> 42.0</td>
      <td> 37.333333</td>
      <td> MATH</td>
      <td> 59.791667</td>
      <td> 42.758333</td>
      <td> D</td>
      <td> DS0</td>
    </tr>
    <tr>
      <th>41886821</th>
      <td>   0</td>
      <td> 50</td>
      <td> 57.5</td>
      <td> 35.833333</td>
      <td> EECS</td>
      <td> 60.833333</td>
      <td> 45.166667</td>
      <td> D</td>
      <td> DS0</td>
    </tr>
    <tr>
      <th>41935225</th>
      <td>  80</td>
      <td> 60</td>
      <td> 52.5</td>
      <td> 64.166667</td>
      <td> BIOL</td>
      <td> 62.500000</td>
      <td> 61.500000</td>
      <td> C</td>
      <td> DS7</td>
    </tr>
  </tbody>
</table>
</div>




![png](HW8_files/HW8_61_1.png)


* Repeat the previous question but for the sections instead of the majors.


    score_three.boxplot(column=['PG'],by=['major'])




    <matplotlib.axes.AxesSubplot at 0x10d72ee50>




![png](HW8_files/HW8_63_1.png)


* Create a dataframe with columns the letter grades 'A', 'B', 'C', 'D', and 'F'
and the sections for rows. The value are the percentage of a given letter grade
per section. Display the DataFrame.


    from pandas import crosstab
    sect_lg=crosstab(score_three.section,score_three.LG,margins=True)
    sect_lg.A=sect_lg.A/sect_lg.All
    sect_lg.B=sect_lg.B/sect_lg.All
    sect_lg.C=sect_lg.C/sect_lg.All
    sect_lg.D=sect_lg.D/sect_lg.All
    sect_lg.F=sect_lg.F/sect_lg.All
    sect_lg.All=sect_lg.All/sect_lg.All
    
    print (sect_lg)
    sect_lg.iloc[0:10,0:5].plot(kind="bar")
    #sect_lg[0:5,1:6].plot(kind="bar",normalize=True)
    #sect_lg.plot(kind="bar")

    col_0           A         B         C         D         F  All
    section                                                       
    DS0      0.136364  0.227273  0.318182  0.090909  0.227273    1
    DS1      0.250000  0.333333  0.333333  0.041667  0.041667    1
    DS2      0.450000  0.250000  0.250000  0.000000  0.050000    1
    DS3      0.208333  0.333333  0.166667  0.125000  0.166667    1
    DS4      0.130435  0.260870  0.347826  0.086957  0.173913    1
    DS5      0.259259  0.148148  0.222222  0.222222  0.148148    1
    DS6      0.192308  0.307692  0.384615  0.076923  0.038462    1
    DS7      0.038462  0.423077  0.346154  0.115385  0.076923    1
    DS8      0.200000  0.360000  0.280000  0.120000  0.040000    1
    DS9      0.206897  0.344828  0.310345  0.103448  0.034483    1
    All      0.200803  0.297189  0.297189  0.104418  0.100402    1





    <matplotlib.axes.AxesSubplot at 0x10dcd0150>




![png](HW8_files/HW8_65_2.png)


* Plot the DataFrame above as a bar plot.


    

* Create a dataframe with columns the letter grades 'A', 'B', 'C', 'D', and 'F'
and the majors for rows. The value are the percentage of a given letter grade
per major. Display the DataFrame.


    

* Plot the DataFrame above as a bar plot.


    

* Explain what you see in the two last plots.




    
