import os, sys


def copy_file(command: str) -> None:
    os.chdir(os.path.dirname(sys.argv[0]))
    
    if not command:
        return "command is empty..."

    cmd = command.split(' ')
    if not len(cmd) == 3:
        return "invalid format..."
    
    origin, new = cmd[1], cmd[2]
    if not os.path.exists(origin):
        return "reference not exists..."
    
    if origin == new:
        return "new file must have a unique name..."
    
    if new in os.listdir(os.getcwd()):
        return "copyfile name has already used in current dir..."
    
    with open(origin, 'r') as origin, open(new, 'a') as new:
            new.write(origin.read())