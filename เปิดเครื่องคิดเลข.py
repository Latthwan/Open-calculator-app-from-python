import os
choice = 0
filename =''
def menu():
    global choice
    print('Menu \n 1.calculator \n 2.notepad \n 3.exit')
    choice = input('Enter number of menu:')
def opennotepad():
    filename = 'c:\\windows\\notepad.exe'
    print('Note by %s'%filename)
    os.system(filename)
def opencalculator():
    filename = 'c:\\windows\\system32\\calc.exe'
    print('Calculate by %s'%filename)
    os.system(filename)
while True:
    menu()
    if choice == '1':
        opencalculator()
    if choice == '2':
        opennotepad()