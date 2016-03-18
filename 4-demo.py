class_name_to_roster = {}

accept_input = True
while accept_input:

    print('Student name?')
    student_name = input('> ')
    accept_input = student_name != 'done'

    if accept_input:
        print('What class is ' + student_name + ' in?')
        class_name = input('> ')

        if class_name in class_name_to_roster:
            old_roster = class_name_to_roster[class_name]
        else:
            old_roster = set()
        new_roster = old_roster | {student_name}
        class_name_to_roster[class_name] = new_roster

print(class_name_to_roster)
