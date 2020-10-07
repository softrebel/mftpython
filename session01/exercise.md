# Session 1 Exercises

## 1. Compare two numbers:

<div dir="rtl">

- الگوریتمی بنویسید که دو مقدار را از ورودی خوانده و مقدار بزرگتر را چاپ کند

### حالات مختلف مقایسه:

</div>
[×] A > B

[×] A < B

[×] A = B

<div dir="rtl">

### فارسی

1. عدد اول را بخوان و بعنوان A در نظر بگیر
2. عدد دوم را بخوان و بعنوان B در نظر بگیر
3. اگر A از B بزرگتر بود، آنگاه A را چاپ کن
4. **در غیر اینصورت اگر** B از A بزرگتر بود B را چاپ کن
5. **در غیر اینصورت اگر** A با B مساوی باشد. عبارت مساوی را چاپ کن
6. پایان
</div>

### English

1. read first number as A.
2. read second number as B.
3. if variable A greater than B: print A
4. **else if** variable B greater than A: print B
5. **else if** variable B equal than A: print equal
6. end



## 2. Read N Numbers and calculate sum.

<div dir="rtl">

- الگوریتمی بنویسید که تعداد N عدد را از ورودی خوانده و مجموع آنها را محاسبه و چاپ کند.
</div>

### Counting:

- counting 1 to N : N times
- counting 0 to N : N+1 times

<div dir="rtl">

### فارسی

1. N را در نظر بگیر
1. i را برابر صفر قرار بده
1. sum را برابر صفر قرار بده
   1. یک عدد از ورودی بخوان و در a بریز
   1. sum = sum + a
   1. i را یک واحد اضافه کن
   1. اگر i < N آنگاه برو به (1)
1. مقدار Sum را نمایش بده (چاپ کن)
1. پایان
</div>

### English

1. load N.
1. sum =0.
1. i=0.
   1. read number from input and assign it to a
   1. sum = sum + a
   1. i = i + 1
   1. if i < N then go to (1)
1. print sum
1. end
<div dir="rtl">

- چون i را از صفر شروع کرده ایم برای اینکه به تعداد N بار فرایند تکرار شود و پس از آن خاتمه یابد، شرط i < N را گذاشتیم(یعنی وقتی i برابر N شود دیگر فرایند تکرار نمی‌شود). حال اگر i را برابر یک قرار داده و می‌خواستیم N بار فرایند تکرار شود، باید از شرط i <= N استفاده می‌کردیم

</div>
