# write your code here
def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "cp":
        old_file, new_file = command[1:]
    if old_file == new_file:
        return
    with open(old_file, "r") as old_file, open(new_file, "w") as new_file:
        new_file.write(old_file.read())
