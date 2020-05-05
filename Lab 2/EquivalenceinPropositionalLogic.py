from logic import TruthTable

myTable = TruthTable(['q or p'])

not_a = TruthTable(['-a'])   
a_and_b = TruthTable (['a and b']) 
a_or_b = TruthTable(['a or b'])   
if_a_then_b = TruthTable(['a <-> b']) 
a_if_and_only_if_b = TruthTable(['a <-> b'])

myTable = TruthTable(['p and q', 'p or q'])
print(myTable.table)

for row in myTable.table:
    print(row)
    prop_values = row[1]
    print("prop_values = {}".format(prop_values))
    #To do check the equivalance of propositions
def propostion1():
    print("The propositions are equivalent")

def propostion2():
    print("The propositions are equivalent")

def propostion3():
    print("The propositions are equivalent")


           
pro1 = input("Enter proposition 1:")
pro2 = input("Enter proposition 2:")

myTable = TruthTable([pro1, pro2])
equivalent = True
for row in myTable.table:
    prop_values = row[1]
    if prop_values[0] != prop_values[1]:
        equivalent = False
        break
    
if equivalent:
    print("The propositions are equivalent")
else:
    print("The propositions are not equivalent")
        
      
if pro1 == "p and p" and pro2 == "q and q":
      proposition1()
if pro1 == "p and q" and pro2 == "q and p":
      propostion2()

if pro1 == "p and q" and pro2 == "q or p":
      propostion3()


