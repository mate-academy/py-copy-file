import os

def copy_file(command: str):
    parts = command.strip().split()
    
    if len(parts) != 3 or parts[0] != "cp":
        return
    
    source, target = parts[1], parts[2]
    
    if source == target:
        return
    
    if not os.path.isfile(source):
        return
    
    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
