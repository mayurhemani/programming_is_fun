

class TelephoneDirectory:
    def __init__(self):
        self.entries = {}

    def add(self, name, phoneNo):
        self.entries[name.lower()] = phoneNo

    def get(self, name):
        return self.entries[name.lower()]

    def update(self, name, phoneNo):
        if name.lower() in self.entries:
            self.entries[name.lower()] = phoneNo
            return True
        return False

    def search(self, name):
        return self.entries[name.lower()]




def menu_function():
    print("To ADD enter A")
    print("To GET something enter G")
    print("To UPDATE enter U")
    print("To SEARCH enter S")
    print("To Quit enter Q")
    return input("Enter your choice: ")


opt = ""
tel = TelephoneDirectory()
while opt != "Q":
    opt = menu_function()

    if opt == "A":
        name = input("Name: ")
        pn = int(input("Phone no: "))
        tel.add(name, pn)

    elif (opt == "G") or (opt == "S"):
        name = input("Name: ")
        print("Phone no = " + str(tel.get(name)))

    elif opt == "U":
        name = input("Name: ")
        pn = int(input("Phone no: "))
        if tel.update(name, pn):
            print("Updated successfully")
        else:
            print("Failed to update. Entry does not exist")



