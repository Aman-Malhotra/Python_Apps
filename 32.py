class Parent:

    def print_last_name(self):
        print('Malhotra')


class Child(Parent):

    def print_first_name(self):
        print('Aman')

    def print_last_name(self):
        print('Sharma')


aman = Child()
aman.print_first_name()
aman.print_last_name()
