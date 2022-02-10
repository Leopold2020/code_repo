
class NTI_Elev:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


    def __str__(self):
        return f"NTI eleven heter {self.name}, de är {self.age} år gammal och är en {self.sex}."

    def return_name(self):
        return self.name



class ITaren(NTI_Elev):

    def __init__(self, name, age, sex, cleanness):
        super().__init__(name, age, sex)
        self.cleanness = cleanness

    def __str__(self):
        return super().__str__() + f" {self.name} är {self.cleanness} ren"

    
def main():
    Person1 = ITaren("Armand", "17", "Man", "Helt ok")
    Person2 = ITaren("Bryan", "18", "Man", "inte")

    # print(armand)
    # print(bryan)


    ITare = [Person1, Person2]
    for ITaren in ITare:
        print(ITaren)

if __name__ == "__main__":
    main()
    