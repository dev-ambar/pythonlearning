class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("configuration of Computer is", self.ram, self.cpu)


com1 = Computer('i3', 16)
com2 = Computer('Atom', 32)
com1.config()
com2.config()
