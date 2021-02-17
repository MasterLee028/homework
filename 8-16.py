#8-16
import module_name
names = ['lee','tom','zhang','wang']
module_name.print_name(names)
from module_name import print_name
print_name(names)
from module_name import print_name as pn
pn(names)
import module_name as mn
mn.print_name(names)
from module_name import *
print_name(names)