from time import sleep

class Person:
    def __init__(self, name, surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __del__(self):
        print("Good luck, " + self.name + " " + self.surname)

    def info(self):
        #return "{0} {1}, {2}".format(self.name, self.surname, self.qualification)
        return "Name: " + self.name + "\nSurname: " + self.surname + "\nQualification: " + str(self.qualification)

unit1 = Person("Nick", "Jester", 0)
unit2 = Person("Alan", "Hopper", 2)
unit3 = Person("Ed", "Sheeran", 1)

command_list = [
    'Show me list of units',
    'Fire unit(number of unit)',
    'End the program',
]

for command in command_list:
    print(command)
    sleep(0.3)

flag = True
while flag:
    print('Please, enter the command: ')
    command = input()
    command_split = command.split()
    for element in command_split:
        if element == 'list':
            print(unit1.info() + "\n")
            print(unit2.info() + "\n")
            print(unit3.info() + "\n")
            break
        elif element == 'Fire':
            if command_split[1] == 'unit1':
                del unit1E
            elif command_split[1] == 'unit2':
                del unit2
            elif command_split[1] == 'unit3':
                del unit3
            else:
                print("Unknown unit")
            break
        elif element == 'End':
            print("End of the program")
            flag = False
        else:
            if element == len(command_split)-1:
                print("Try again")
            else:
                pass



"""
while True:
    last_msg = input()
    if last_msg == "Enter":
        break
"""