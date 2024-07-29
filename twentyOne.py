current_number = 1

def count_up(number):
    for i in range(3):
        number += 1
        print(number)
    return number

new_list = []

for i in range(1,22):
    new_list.append(i)

#for i in new_list:
#    print(i)

for i in range(21):

    stng = new_list[0], new_list[1], new_list[2]
    choice = int(input(stng))

    if choice == new_list[0]:
        new_list.pop(0)
    elif choice == new_list[1]:
        new_list.pop(0)
        new_list.pop(0)
    elif choice == new_list[2]:
        new_list.pop(0)
        new_list.pop(0)
        new_list.pop(0)



#while current_number < 21:
#    stng = current_number, current_number + 1, current_number + 2
#    input(str(stng))
#    current_number = count_up(current_number)


