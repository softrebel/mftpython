a=[1,2,3,4,421,343,1221,234,'ali']

def slice(alist):
    return alist[-5:400]

#temp=slice(a)
#print(temp)
# print(a)
# for item in range(3,5):
#    a.pop(item)
# print(a)



def sliceEven(alist):
    count=len(alist)
    return alist[0:count:2]
    return alist[0::2]
    #return alist[0:-1:2]

#temp=sliceEven(a)


def slice3(alist):
    return alist[::3]
    #return alist[0::3]
    #count=len(alist)
    #return alist[0:count:3]
    #return alist[:count:3]





#print(a)
#temp=slice3(a)
#print(temp)

#a='ali'
#b="ali"
#c=""" salam
#khubi che khabar

#"""
#print(a)
#print(b)
#print(c)

def stringify(alist):
    result=''
    for item in alist:
        result=result+str(item)
    return result


#a=[22,3,44,55,64]
#print(a)
#print(stringify(a))

a=[1,2,3,4]

def stringify2(alist):
    for item in alist:
        result=str(item)*item
        print(result)


#stringify2(a)

a='alireza'

def stringify3(string):
    #return string[::2]
    return string[::-2]

print(a)
b=stringify3(a)
print(b)





