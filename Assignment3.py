q1.Sample List : (8, 2, 3, 0, 7)

Expected Output : 20
def sum(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
list=[8,2,3,0,7]
sum(list)

q2.def reverse(n):
    string=""
    for i in n:
        string=(n[::-1])
    return string
n="1234abcd"
reverse(n)

q3.def calculate(letters):
    count1=0
    count2=0
    for char in letters:
        if char.isupper():
            count1 += 1
        elif char.islower():
            count2 += 1
    print("no. of upper case characters:",count1)
    print("no of lower case characters:",count2)
l ="The quick Brow Fox"
calculate(l)