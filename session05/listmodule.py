def sumlist(a):
    sum=0
    for item in a:
        sum=sum+item
    return sum

def greater(a):
    max=a[0]
    for item in a:
        if item > max:
            max=item


def tafriq(a):
    diff=2*a[0]
    for item in a:
        diff=diff-item

    return diff

