from person import Person


class Family:
    def __init__(self, ancestorName, ancestorSex, ancestorParent, isAncestorAlive):
        self.tree = Person(ancestorName, None, ancestorParent, isAncestorAlive)
        self.ancestorName = ancestorName
        self.ancestorSex = ancestorSex
        self.ancestorParent = ancestorParent
        self.finder = None
        self.patternFinder = None

    def __find(self, name, node):
        if node.name == name:
            self.finder = node
        for child in node.children:
            self.__find(name, child)

    def __pattern(self, name, node, pattern):
        if node.name == name:
            self.patternFinder = pattern
        for child in node.children:
            self.__pattern(name, child, pattern + [self.findPerson(child.parent)])

    def findPerson(self, name):
        self.finder = None
        self.__find(name, self.tree)
        return self.finder

    def __patternToRelation(self, pattern):
        result = []
        for i in range(len(pattern)-1):
            result.append(self.__siblingChildRelation(pattern[i], pattern[i+1]))
        return result

    def __findPattern(self, name):
        self.patternFinder = None
        self.__pattern(name, self.tree, [])
        return (self.patternFinder + [self.findPerson(name)])

    def relation(self, first, second):
        if first == second:
            raise Exception('Same Person is not possible for detection!')

        FP = self.__findPattern(first)  # First Pattern
        SP = self.__findPattern(second)  # Second Pattern
        i = j = 0
        while i < len(FP) and j < len(SP) and FP[i] == SP[j]:
            i += 1
            j += 1

        pattern = ' '.join(self.__patternToRelation(FP[i:][::-1] + SP[j:]))
        relations = {
            'khahar pedar': 'ame',
            'khahar madar': 'khaleh',
            'baradar pedar': 'amoo',
            'baradar madar': 'dayie',
            'pesar pesar': 'nave pesari',
            'pesar dokhtar': 'nave pesari',
            'dokhtar pesar': 'nave dokhtari',
            'dokhtar dokhtar': 'nave dokhtari',
            'pedar pedar': 'pedarbozorg',
            'pedar madar': 'pedarbozorg',
            'madar pedar': 'madarbozorg',
            'madar madar': 'madarbozorg',
        }
        for k, v in relations.items():
            pattern = pattern.replace(k, v)

        if first == self.ancestorName:
            pattern = ('pedar ' if self.ancestorSex ==
                       'm' else 'madar ') + pattern

        if second == self.ancestorName:
            pattern += (' dokhtar' if FP[1].sex == 'f' else ' pesar')

        return pattern

    def newChild(self, name, parent, partner=None, isAlive=True):
        parentNode = self.findPerson(parent)
        parentNode.children.append(Person(name, parent, partner, isAlive))

    def newChildren(self, parent, children):
        parentNode = self.findPerson(parent)
        parentNode.children.extend(children)

    def numberOfChildren(self, name):
        return len(self.findPerson(name).children)

    def __siblingChildRelation(self, first, second):
        if first.parent == second.name:
            return 'pesar' if first.sex == 'm' else 'dokhtar'

        elif first.parent == second.parent:
            return 'khahar' if first.sex == 'f' else 'baradar'

        elif first.name == second.parent:
            return 'pedar' if first.sex == 'm' else 'madar'

        else:
            return None

    def __printFamilyTree(self, node, spaces):
        if not node:
            return
        print(spaces+node.name)
        for child in node.children:
            self.__printFamilyTree(child, spaces + '    ')

    def PrintFamilyTree(self):
        self.__printFamilyTree(self.tree, '')
