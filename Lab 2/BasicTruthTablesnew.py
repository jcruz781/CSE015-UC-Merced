from logic import TruthTable



not_a = TruthTable(['-a'])
not_a.display()

a_and_b = TruthTable (['a and b'])
a_and_b.display()

a_or_b = TruthTable(['a or b'])
a_or_b.display()

if_a_then_b = TruthTable(['a -> b'])
if_a_then_b.display()

a_if_and_only_if_b = TruthTable(['a <-> b'])
a_if_and_only_if_b.display()


