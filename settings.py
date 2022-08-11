from collections import namedtuple, OrderedDict



Usernp = namedtuple('User',('Name', 'Username', 'Password', 'Token', 'Profile'))
Miriam = Usernp(*('Miriam','miriam','supersabia','','admin'))
Alberto = Usernp(*('Alberto','beto','zapato','','admin'))
users = OrderedDict()
users['alberto'] = Alberto
users['miriam'] = Miriam


