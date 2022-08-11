from collections import namedtuple, OrderedDict



Usernp = namedtuple('User',('Name', 'Username', 'Password', 'Token', 'Profile'))
Alberto = Usernp(*('Alberto','beto','zapato','','admin'))
users = OrderedDict()
users['alberto'] = Alberto


