#Print each Word in a word list:
words = ["Dignity", "Endurance", "Patience"]
for x in words:
    print(x)
#Loop through the letters in the word "Pace":
for x in "Pace":
    print(x)
#Exit the loop when x is "Second":
num = ["First", "Second", "Third"]
for x in num:
  if x == "Second":
    break
  print(x)
#Exit the loop when x is "Third", but this time the break comes before the print:
num = ["First", "Second", "Third", "Fourth"]
for x in num:
  print(x)
  if x == "Third":
    break
#Do not print "Second":
num = ["First", "Second", "Third", "Fourth"]
for x in num:
  if x == "Second":
    continue
  print(x) 
________________________________________________
Dignity
Endurance
Patience
P
a
c
e
First
First
Second
Third
First
Third
Fourth

[Program finished]
