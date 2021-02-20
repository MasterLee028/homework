#9-11
from module_admin import User,Privileges,Admin
admin_0 = Admin('lee','tom','20','123@qq.com')
admin_0.privileges.show_privileges()
#9-12
from module_admin_up1 import Privileges,Admin
admin_1 = Admin('tom','curry','19','456@qq.com')
admin_1.privileges.show_privileges()