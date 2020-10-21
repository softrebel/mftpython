#def function_name():
    #statement
    #statement
    #...

    #return

def salam_kon():
    print("salam")
 

#salam_kon()

# Function Types:
# in:false,out:false
# in:true,out:false
# in:false,out:true
# in:true,out:true

def salam_kon1(name):
    print("salam",name)

#salam_kon1("ali")


def name_kamel():
    a='ali'
    b='reza'
    c= a + ' ' +b
    return c

#name=name_kamel()
#print(name)

def sum_two_number(a,b):

    sum=a+b
    return sum


#temp=sum_two_number(2,3)
#print('temp=',temp)


def multiply_two_number(a,b):
    res=a*b
    return res


temp=[1,4,5,12]

def list_sum(list):
    sum=0
    for item in list:
        sum=sum+item
    return sum

#result=list_sum(temp)
#print(result)


def greater(a_list):
    max=a_list[0]
    for item in a_list:
        if item > max:
            max=item
    return max
#temp=[1,4,25,12]
#print(greater(temp))

## list -> min,max -> max-min

a_list=[3,5,2,22,31]

def min_max(a):
    min=a[0]
    max=a[0]
    for item in a:
        if item > max:
            max=item
        if item < min:
            min=item
    return max-min

result=min_max(a_list)
print(result)




























