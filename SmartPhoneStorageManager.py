class Smartphone:
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.left = self.capacity
        self.name = name
        self.total = 0
        self.dict = {}
        print("Smartphone created!")
        
    def add_app(self, appname, appsize):
        self.appname = appname
        self.appsize = appsize
        
        if self.appname in self.dict:
            print("Rejected; app already exists")
        elif self.left-self.appsize > 0:
            self.dict[self.appname] = self.appsize
            self.left-=self.appsize
            self.total += self.appsize
            #print(self.dict)
        elif self.left-self.appsize <= 0:
            print("Cannot install app, no available space")
        print()
    def remove_app(self, appname):
        self.appname = appname
        if self.appname in self.dict:
            app = self.dict.get(self.appname)
            self.total -= app
            self.left += app
            del self.dict[self.appname]
            print("App removed:", self.appname)
        else:
            print ('This app does not exist')
        print ()

    def has_app(self, appname):
        self.appname = appname
        if self.appname in self.dict:
            return True
        else:
            return False
        
        print ()

    def get_available_space(self):
        return self.left
    
    def report(self):
        print("Name:", self.name)
        print("Capacity:", self.total, "out of", self.capacity, "GB")
        print("Available space:", self.left, "GB")
        print("# of apps installed:", len(self.dict))
        sorted_dict = dict(sorted(self.dict.items()))
        for key,value in sorted_dict.items():
            print('-',key, "is using", value, "GB")
        
        print()

size = int(input("Size of your new smartphone: "))
name = input("Smartphone name: ")
phone = Smartphone(size,name)
phone.report()
option = input ('(r)eport, (a)dd app, r(e)move app or (q)uit: ').lower()

while option != 'q':
    
    if option == 'r':
        phone.report()

    elif option == 'a':
        app_name = input ("App name to add: ")
        app_size = int (input ("App size in GB: "))
        phone.add_app(app_name, app_size)

    elif option == 'e':
        rem = input ("App name to remove: ")
        phone.remove_app(rem)

    option = input ('(r)eport, (a)dd app, r(e)move app or (q)uit: ').lower()

if option == "q":
    print("Goodbye!")
