# write your code here
def copy_file(command: str) -> None:
    old_file = command.split()[1]
    new_file = command.split()[2]
    if old_file != new_file and command.split()[0] == "cp":
        with open(old_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
