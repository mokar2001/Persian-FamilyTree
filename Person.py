class Person:
    def __init__(self, name, parent, sex, partner=None, isAlive=True):
        self.name = name
        self.partner = partner
        self.parent = parent
        self.isAlive = isAlive
        self.children = []
        self.sex = sex
