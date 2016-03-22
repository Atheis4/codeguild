# Initialize variables
class_name_to_roster = {}
accept_input = True

# while loop = as long as true, continue to accept input for student name.
while accept_input:

    student_name = input('Student name?\n> ')
    accept_input = student_name != 'done'

    # if statement = if acceptable input for student name,
    if accept_input:
        class_name = input('What class is ' + student_name + ' in?\n> ')

        if class_name in class_name_to_roster:
            old_roster = class_name_to_roster[class_name]
        else:
            old_roster = set()
        new_roster = old_roster | {student_name}
        class_name_to_roster[class_name] = new_roster

print(class_name_to_roster)
