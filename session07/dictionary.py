## dictionary
# [1,2,3]
# [[1,2],[3,4]]
# 'str'
# 23

# {"key":"value","key1","value1"}
from collections import defaultdict

#a=defaultdict(int)
#a['ali']='reza'
#print(a['mamad'])


# value sorted
a={"ali":12,"mamad":20,"bagher":16}

def sorted_keys(a_dict):
    result=[]
    values=a_dict.values()
    for i in values:
        result.append(i)
    result.sort()
    return result # result.sort()

#print(sorted_keys(a))


a={'ali': [1,4,6], 'arad': [6,7,10], 'amir': [10,4,2,6]}

#for i in range(1,3):
    #print(i)
    # i=1 -> print
    # i=2 -> print
    
    
#for k,v in a.items():
    #print(k,v)

a={'ali': [1,4,6], 'arad': [6,7,10], 'amir': [10,4,2,6]}
# a, 6 -> ['ali','arad','amir']  'in'
def find_in_dict(a_dict,adad):
    result=[]
    for k,v in a_dict.items():
        if adad in v:
            result.append(k)
    return result
#print(find_in_dict(a,11))

def number_to_word(a):
    result=''
    word_dict={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"
        }
    for i in a:
        result=result+word_dict[int(i)]+' ' # a['ali'], a[2]
    return result

#print(number_to_word('233'))
            

# s = 'alireza'
# a_dict={'a':2,'l':1,...}

def freq_dict(s):
    result={}
    for i in s:
        count=s.count(i)
        result[i]=count
    return result

#print(freq_dict("amirhosein"))

