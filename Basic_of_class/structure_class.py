class Animal:

    name_of_animal = ' '

    def __init__(self, nameofanimal):
        print('this is class init method')
        print('selef',self)
        print('selef',self)
        self.name_of_animal = nameofanimal
        print('animal_name = ',self.name_of_animal)

an1 = Animal('dog')   