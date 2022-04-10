#P-1=Write a program to iterate the 7 numbers and in each iteration, print the sum of the current and previous number
print("Printing present number and previous number and their sum in a range(7)")
previous_num = 0

# loop from 1 to 7
for a in range(1, 7):
    sum = previous_num + a
    print("Present Number", a, "Previous Number ", previous_num, " Sum: ", previous_num + a)
    # modify previous number
    # set it to Present number
    previous_num = a
_______________________________________
Printing present number and previous number and their sum in a range(7)
Present Number 1 Previous Number  0  Sum:  1
Present Number 2 Previous Number  1  Sum:  3
Present Number 3 Previous Number  2  Sum:  5
Present Number 4 Previous Number  3  Sum:  7
Present Number 5 Previous Number  4  Sum:  9
Present Number 6 Previous Number  5  Sum:  11

[Program finished]
