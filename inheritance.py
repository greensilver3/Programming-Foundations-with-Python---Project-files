class Parent():
    def __init__(self, last_name, eye_color):
        print(" Parent constructor called ")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_degress):
        print(" Child constructor called ")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_degress = number_of_degress
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of degress - "+str(self.number_of_degress))
        
#anebajagane_venugopal = Parent("Anebajagane","brown")
#anebajagane_venugopal.show_info()
#print(anebajagane_venugopal.last_name)


gautham_anebajagane = Child("Anebajagane","brown", 2)
gautham_anebajagane.show_info()
print(gautham_anebajagane.last_name)
print(gautham_anebajagane.number_of_degress)
