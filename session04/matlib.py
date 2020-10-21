def min_max(a):
    min=a[0]
    max=a[0]
    for item in a:
        if item > max:
            max=item
        if item < min:
            min=item
    return max-min
