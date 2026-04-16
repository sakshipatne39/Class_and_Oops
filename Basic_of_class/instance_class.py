class Animal:

    name_of_animal = 'start '
    Animal_sound = 'start'


    def __init__(self, nameofanimal, animalsound):
        
        self.name_of_animal = nameofanimal
        self.Animal_sound = animalsound

        print('inside class animal name = ',self.name_of_animal)
        print('inside class animal sound = ',self.Animal_sound)

an1 = Animal('dog', 'bark')
print('outside class animal_name = ',an1.name_of_animal)
print('outside class animal_sound = ',an1.Animal_sound)   

print('')
print('')
print('')
print('')
an2 = Animal('cat', 'meow')
