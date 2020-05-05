from logic import TruthTable

myTable = TruthTable(['p or q'])
myTable.display()
not_a = TruthTable(['-a'])
a_and_b = TruthTable (['a and b'])
a_or_b = TruthTable(['a or b'])
if_a_then_b = TruthTable(['a <-> b'])
a_if_and_only_if_b = TruthTable(['a <-> b'])

