class student:
    def __int__(self,name,age,gender,sex_type):
        self.name = name
        self.age = age
        self.gender = gender
        self.sex_type  = sex_type

    def input(self,name,age,gender,sex_type):
        self.name = name
        self.age = age
        self.gender = gender
        self.sex_type  = sex_type
        self.name = input("input a name")
        self.age = input("input an age")
        self.gender = input("input a gender")
        self.sex_type = input("input a gender")

        print(self.name +    str(self.age) +   self.gender +   self.sex_type)
        
        
joy = student()
joy.input('favour',20,'male','boy')