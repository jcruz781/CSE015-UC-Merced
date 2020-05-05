from logic import TruthTable

p1 = 'p and q'
p2 = 'p or q'

stop = False

props = []

while not stop:
    p = input('Enter a proposition: ')
    props.append(p)
    enter_more = input('Would you like to enter more Y/N: ')
    if enter_more == 'N':
        stop = True
    elif enter_more == 'Y':
        stop = False
    else:
        print('Not a valid input')
        exit()

tt = TruthTable(props)
tt.display()


is_consistent = False
for row in tt.table:
    var_values = row[0]
    prop_values = row[1]

    temp = True
    for p in prop_values:
        temp = temp and p
    if temp == True:
       is_consistent = True

if is_consistent == True:
    print('Your description is consistent')
else:
    print('Your description is NOT consitent')
    
    

   
