# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

from sys import argv

class App(object):
    def __init__(self):
        self.start_screen()

    def start_screen(self):
        print(str("here is your fav animals: " + str(self.list_printer())))


    def check_argument(self):
        arg = self.get_arguments()
        if arg == None:
            self.start_screen()
        elif arg == '-add':
            self.check_animal_in_list()
            self.add_animal()
        return argv[2]            

    def get_arguments(self):
        temp_containded_animal = []
        temp_containded_animal.append(argv[2])
        if len(argv) >1:
            return argv[1]
        return None

    def read_list(self):
        raw_list = []
        list_of_animals = open('favourites.txt', "r")
        for line in list_of_animals:
            raw_list.append(line)
        return raw_list
                    
    def check_animal_in_list(self):
        fav_animal = self.read_list()
        for temp_containded_animal in fav_animal:
            if temp_containded_animal == fav_animal:
                print("this animal is already on your list")

    def list_printer(self):
        raw_list = self.read_list()
        print('\n')
        list_of_fav_animals = []
        line_counter = 0
        printed_animals = []
        for line in raw_list:
            line_counter += 1
            print(line)
        return list_of_fav_animals


    def add_animal(self):
        with open("favourites.txt", 'a') as list_of_animals:
            list_of_animals.write(argv[2]+ '\n')
        return self.list_printer()
    
    # def run(self):
    #     self.check_argument()
cli_screen = App()
cli_screen.check_argument()