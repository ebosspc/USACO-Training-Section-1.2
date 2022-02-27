"""
ID: e.franc1
LANG: PYTHON3
TASK: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

# Create variables for the comet and group names from the input
words_list = []
for line in fin:
    word = line.strip()
    words_list.append(word)
comet_name = words_list[0]
group_name = words_list[1]

# Create lists with the numerical equivalents of each of the names' letters
comet_char_vals_list = []
group_char_vals_list = []
for char in comet_name:
    if char == 'A':
        comet_char_vals_list.append(1)
    if char == 'B':
        comet_char_vals_list.append(2)
    if char == 'C':
        comet_char_vals_list.append(3)
    if char == 'D':
        comet_char_vals_list.append(4)
    if char == 'E':
        comet_char_vals_list.append(5)
    if char == 'F':
        comet_char_vals_list.append(6)
    if char == 'G':
        comet_char_vals_list.append(7)
    if char == 'H':
        comet_char_vals_list.append(8)
    if char == 'I':
        comet_char_vals_list.append(9)
    if char == 'J':
        comet_char_vals_list.append(10)
    if char == 'K':
        comet_char_vals_list.append(11)
    if char == 'L':
        comet_char_vals_list.append(12)
    if char == 'M':
        comet_char_vals_list.append(13)
    if char == 'N':
        comet_char_vals_list.append(14)
    if char == 'O':
        comet_char_vals_list.append(15)
    if char == 'P':
        comet_char_vals_list.append(16)
    if char == 'Q':
        comet_char_vals_list.append(17)
    if char == 'R':
        comet_char_vals_list.append(18)
    if char == 'S':
        comet_char_vals_list.append(19)
    if char == 'T':
        comet_char_vals_list.append(20)
    if char == 'U':
        comet_char_vals_list.append(21)
    if char == 'V':
        comet_char_vals_list.append(22)
    if char == 'W':
        comet_char_vals_list.append(23)
    if char == 'X':
        comet_char_vals_list.append(24)
    if char == 'Y':
        comet_char_vals_list.append(25)
    if char == 'Z':
        comet_char_vals_list.append(26)    
for char in group_name:
    if char == 'A':
        group_char_vals_list.append(1)
    if char == 'B':
        group_char_vals_list.append(2)
    if char == 'C':
        group_char_vals_list.append(3)
    if char == 'D':
        group_char_vals_list.append(4)
    if char == 'E':
        group_char_vals_list.append(5)
    if char == 'F':
        group_char_vals_list.append(6)
    if char == 'G':
        group_char_vals_list.append(7)
    if char == 'H':
        group_char_vals_list.append(8)
    if char == 'I':
        group_char_vals_list.append(9)
    if char == 'J':
        group_char_vals_list.append(10)
    if char == 'K':
        group_char_vals_list.append(11)
    if char == 'L':
        group_char_vals_list.append(12)
    if char == 'M':
        group_char_vals_list.append(13)
    if char == 'N':
        group_char_vals_list.append(14)
    if char == 'O':
        group_char_vals_list.append(15)
    if char == 'P':
        group_char_vals_list.append(16)
    if char == 'Q':
        group_char_vals_list.append(17)
    if char == 'R':
        group_char_vals_list.append(18)
    if char == 'S':
        group_char_vals_list.append(19)
    if char == 'T':
        group_char_vals_list.append(20)
    if char == 'U':
        group_char_vals_list.append(21)
    if char == 'V':
        group_char_vals_list.append(22)
    if char == 'W':
        group_char_vals_list.append(23)
    if char == 'X':
        group_char_vals_list.append(24)
    if char == 'Y':
        group_char_vals_list.append(25)
    if char == 'Z':
        group_char_vals_list.append(26)    

# Compute the product of each name
comet_product = 1
group_product = 1
for num in comet_char_vals_list:
    comet_product = comet_product * num
for num in group_char_vals_list:
    group_product = group_product * num

# If the mod 47 of both products is the same, output GO, if not STAY
if comet_product % 47 == group_product % 47:
    fout.write ("GO" + '\n')
else:
    fout.write("STAY" + '\n')

fout.close()
