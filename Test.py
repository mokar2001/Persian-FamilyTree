from Person import *
from Family import *
#ancestor
tree = Family('ali', 'm', 'mahrokh', False)

#children of ali
tree.newChildren(
    'ali',
    [
        Person('shahnaz', 'ali', 'f', 'hejir', False),
        Person('shahram', 'ali', 'm', 'elham'),
        Person('hamideh', 'ali', 'f', 'mohamad shafie'),
        Person('hamed', 'ali', 'm', 'fataneh'),
        Person('elham', 'ali', 'f', None),
        Person('iman', 'ali', 'm', None)
    ]
)

#children of shahnaz
tree.newChildren(
    'shahnaz',
    [
        Person('reza', 'shahnaz', 'm', None),
        Person('nima', 'shahnaz', 'm', None),
    ]
)

#children of shahram
tree.newChildren(
    'shahram',
    [
        Person('tarlan', 'shahram', 'f', None),
        Person('radvin', 'shahram', 'm', None),
    ]
)

#children of hamideh
tree.newChildren(
    'hamideh',
    [
        Person('parisima', 'hamideh', 'f', None),
        Person('mohamadreza', 'hamideh', 'm', None),
        Person('mohamadmehdi', 'hamideh', 'm', None),
    ]
)

#children of hamed
tree.newChildren(
    'hamed',
    [
        Person('arshavin', 'hamed', 'm', None),
    ]
)

#children of elham
tree.newChildren(
    'elham',
    [
        Person('bahar', 'elham', 'f', None),
    ]
)

#children of mohamadreza
tree.newChildren(
    'mohamadreza',
    [
        Person('alex', 'mohamadreza', 'm', None)
    ]
)

print(tree.relation('nima', 'alex'))
print(tree.siblingChildRelation(tree.findPerson('iman'), tree.findPerson('elham')))
tree.PrintFamilyTree()