 ## ASSIGNMENT_4

### Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.


```python
Add_25=lambda num:num+25
Add_25(10)
```




    35



### Write a Python program to triple all numbers of a given list of integers. Use Python map.


```python
l=[1,2,3,4,5,6,7]
list(map(lambda l:l*3,l))
```




    [3, 6, 9, 12, 15, 18, 21]



### Write a Python program to square the elements of a list using map() function.


```python
sample_list=[4,5,2,9]
def sqr(x):
        return(x**2)
print('square of elements of given list using map() is',list(map(sqr,sample_list)))
```

    square of elements of given list using map() is [16, 25, 4, 81]



```python

```
