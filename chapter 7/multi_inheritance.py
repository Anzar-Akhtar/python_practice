class Father:

    def father_property(self):
        print("Father has a house")

class Mother:

    def mother_property(self):
        print("Mother has a car")

class Child(Father, Mother):

    def child_property(self):
        print("Child has a bike")


child1 = Child()

child1.mother_property()
child1.father_property()
child1.child_property()



class Coder:

    def code(self):
        print("Writing Code")

class Designer:

    def design(self):
        print("Designing UI")

class Developer(Coder, Designer):

    def develop(self):
        print("Developing Application")

dev = Developer()

dev.code()
dev.design()
dev.develop()



class Father:

    def show(self):
        print("Father")

class Mother:

    def show(self):
        print("Mother")

class Child(Father, Mother):
    pass


child1 = Child()

child1.show()
print(Child.mro())


class Programmer:

    def code(self):
        print("Programmer is coding")


class DevOps:

    def deploy(self):
        print("DevOps Engineer is Deploying")

class DevOpsEngineer(Programmer, DevOps):

    def monitor(self):
        print("DevOps engineer is monitoring")


engineer = DevOpsEngineer()

engineer.code()
engineer.deploy()
engineer.monitor()