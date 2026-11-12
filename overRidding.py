from abc import ABC ,abstractmethod


class animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    def display(self,):
        print('this is a animal ')

class dog(animal):
    def sound(self):
        print('dog barks')    
    def display(self):
        return super().display()   
         
class puppy(dog):
    def sound(self):
        print('puppy barks') 
    def display(self):
        return super().display()    

p = puppy()

p.sound()

p.display()
