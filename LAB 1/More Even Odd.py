my_list = []

for i in range(10):
    number = int(input("number {}: ".format(i)))
    my_list.append(number)

print("my_list = {}".format(my_list))

odd_max = float('-inf')
for num in my_list:
    if num % 2 == 1:
        if num > odd_max:
            odd_max = num

if odd_max > float('-inf'):
    print(odd_max)

else:
    print ("No odd numbers were entered")
