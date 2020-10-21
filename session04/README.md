# Session 04

## Nested For

```
# nested loop example
#for i in range(0,3):
#    // i=0,1,2
#    for j in range(0,3):
#        //j=0,1,2
#        print('*')

# 1-10 -> sum()
for i in range(1,11):
    sum=0
    for j in range(1,i+1):
        sum=sum+j
    print(i,sum)
# exercise:
# min=input()
# max=input()

```

## Function

## Module

## List

## Research

- remove from index of list
- how to remove all of the same item from the list
- how to find all of the same item indexes


## Shell
```
>>> a=[1,3,2]
>>> a
[1, 3, 2]
>>> sorted(a)
[1, 2, 3]
>>> a=sorted(a)
>>> a
[1, 2, 3]
>>> a.sort()
>>> a
[1, 2, 3]
>>> a[0]
1
>>> a[-1]
3
>>> a[-3]
1
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> a[2]
3
>>> a[1]
2
>>> a
[1, 2, 3]
>>> a.insert(1,'ali')
>>> a[1]
'ali'
>>> a
[1, 'ali', 2, 3]
>>> a[1]='amir'
>>> a
[1, 'amir', 2, 3]
>>> a=[1,2,3,4]
>>> a[1]
2
>>> a[0]
1
>>> a[1]
2
>>> a[2]
3
>>> a[3]
4
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a[4]
IndexError: list index out of range
>>> a
[1, 2, 3, 4]
>>> a[1]=25
>>> a
[1, 25, 3, 4]
>>> a.insert(1,2)
>>> a
[1, 2, 25, 3, 4]
>>> a[2]
25
>>> a
[1, 2, 25, 3, 4]
>>> a.insert(-1,'ali')
>>> a
[1, 2, 25, 3, 'ali', 4]
>>> a.insert(-2,'amir')
>>> a
[1, 2, 25, 3, 'amir', 'ali', 4]
>>> a.append(225)
>>> a
[1, 2, 25, 3, 'amir', 'ali', 4, 225]
>>> b=[]
>>> b.appent(1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b.appent(1)
AttributeError: 'list' object has no attribute 'appent'
>>> b.append(1)
>>> b.append(2)
>>> b.append(3)
>>> b[2]=234
>>> b.insert(1,'amir')
>>> b
[1, 'amir', 2, 234]
>>> b.remove('amir')
>>> b
[1, 2, 234]
>>> a=[1,2,3,4,5,6,2,4,5]
>>> a.remove(2)
>>> a
[1, 3, 4, 5, 6, 2, 4, 5]
>>> a=[1,2,3,4,5]
>>> as
SyntaxError: invalid syntax
>>> a
[1, 2, 3, 4, 5]
>>> a.pop()
5
>>> a
[1, 2, 3, 4]
>>> a.pop(1)
2
>>> b=[1,4,254,11,24]
>>> a
[1, 3, 4]
>>> b.remove(11)
>>> b.pop(1)
4
>>> b.insert(2,'ali')
>>> b.append(23)
>>> b
[1, 254, 'ali', 24, 23]
>>> b.pop()
23
>>> a=[1,2,3,4]
>>> a.index(1)
0
>>> a=['ali','amir','reza']
>>> a.index('ali')
0
>>> a.index('reza')
2
>>> a=[1,2,3,4,2,1,2]
>>> a.index(2)
1
>>> a=[1,2,3,4,5,6]
>>> a.reverse()
>>> a
[6, 5, 4, 3, 2, 1]
>>> a[2]
4
>>> a=['ali','reza',2,'amir']
>>> a.reverse()
>>> a
['amir', 2, 'reza', 'ali']
>>> a[2]
'reza'
>>> a.index('reza')
2
>>>


```
