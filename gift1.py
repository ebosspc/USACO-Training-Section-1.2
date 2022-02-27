"""
ID: e.franc1
LANG: PYTHON3
TASK: gift1
"""
fin = open('input.txt', 'r')

# Create a list containing input data
input_data = []
for line in fin:
    gift_data = line.strip()
    if ' ' in gift_data:
        parts = gift_data.split(' ')
        gift_data = parts
    input_data.append(gift_data)

person_1 = ''
person_2 = ''
person_3 = ''
person_4 = ''
person_5 = ''
person_6 = ''
person_7 = ''
person_8 = ''
person_9 = ''
person_10 = ''
num_people = input_data[0]

print(input_data)





# fout = open('gift1.out', 'w')
# fout.close()