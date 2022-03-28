Num= ["Natural", "Whole", "Integers", "Rational", "Irrational", "Real", "Complex"]
print (Num*2)
print (len(Num))
Num.append("Fraction")
print (Num)
Num.insert(2, "Prime")
print (Num)
Num.remove("Irrational")
print (Num)
Num.sort()
print (Num)
Num.reverse()
print (Num)
Num.pop()
Num.pop()
print (Num)
Num2=Num.copy()
print (Num2)
pos=Num.index("Whole")
print (pos)
________________________________________________
['Natural', 'Whole', 'Integers', 'Rational', 'Irrational', 'Real', 'Complex', 'Natural', 'Whole', 'Integers', 'Rational', 'Irrational', 'Real', 'Complex']
7
['Natural', 'Whole', 'Integers', 'Rational', 'Irrational', 'Real', 'Complex', 'Fraction']
['Natural', 'Whole', 'Prime', 'Integers', 'Rational', 'Irrational', 'Real', 'Complex', 'Fraction']
['Natural', 'Whole', 'Prime', 'Integers', 'Rational', 'Real', 'Complex', 'Fraction']
['Complex', 'Fraction', 'Integers', 'Natural', 'Prime', 'Rational', 'Real', 'Whole']
['Whole', 'Real', 'Rational', 'Prime', 'Natural', 'Integers', 'Fraction', 'Complex']
['Whole', 'Real', 'Rational', 'Prime', 'Natural', 'Integers']
['Whole', 'Real', 'Rational', 'Prime', 'Natural', 'Integers']
0

[Program finished]
