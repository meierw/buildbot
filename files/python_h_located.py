from os.path import isfile
from sysconfig import get_paths
print(isfile(get_paths()['include'] + '/Python.h'))
