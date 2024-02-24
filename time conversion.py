my_list = input("")
split_chars = []
for string in my_list:
    for char in string:
        split_chars.append(char)
print(split_chars)
c=split_chars[:-2]
balance=split_chars[2:8]
print("time is ", balance)
g=''.join(balance)
print(g)
if 'p,m' or 'P,M' in c:
    d=c[0:2]
    print(d)
    concatenated_string = ''.join(d)
    print(concatenated_string)
    e=0
    concatenated_string=int(e)
    t = e  # Example string representing a number
    t_as_int = int(t)  # Convert the string to an integer
    result = t_as_int + 12
    print(result)
    list1=list(result).split(' ')
    
    converted_time=
    print(converted_time)
else:
    print('false')
