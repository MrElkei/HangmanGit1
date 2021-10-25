# Kods ņemts no https://www.delftstack.com/howto/python/python-clear-console/
# TODO add this to Game object
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)