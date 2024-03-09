from integer_list import IntegerList

int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 49
print('Inserting int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('8-10')
except ValueError as e:
    print(e)

try:
    int_list[0] = '10/11'
except ValueError as e:
    print('Inserting string failed:', e)

try:
    int_list.extend([997, '10/11'])
except ValueError as e:
    print('Extending with ineligible element failed:', e)

int_list += [7]

print('Before insert:', int_list)
int_list.insert(2, 99)

print('Final result:', int_list)
