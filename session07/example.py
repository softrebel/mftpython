## Session 07


# str -> a -> upper
# str -> b -> lower
# str -> ... -> str

def change_string(s):
    result=''
    if s.find('a') != -1:
        result= s.upper()
    elif s.find('b') != -1:
        result=s.lower()
    else:
        result=s

    return result

#print(change_string('abbas'))
#print(change_string('bb'))
#print(change_string('vis'))


def go_up_a(s):
    return s.replace('a','A')

#print(go_up_a('salam'))

a=[[1,2],[3,4],[5,6]]
z=1
for i in a:
    for j in i:
        z=z*j


#print(z)
a_list=[['ali',12,16,18],['amir',20,19,13],['arad',15,16,19]]

def average(a):
    for i in a:
        result=i[0]+':'
        sum=0
        for j in i[1:]:
            sum=sum+j
        result=result+str(sum/3)
        print(result)
average(a_list)
        

