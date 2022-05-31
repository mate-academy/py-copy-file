def copy_file(command: str):
    name1, name2 = command.split()[1], command.split()[2]
    if name1 != name2:
        with open(name1, 'r') as f1:
            with open(name2, 'w') as f2:
                f2.write(f1.read())
