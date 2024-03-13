# write your code here
def copy_file(command: str) -> None:
    command = command.split()
    if command[1] == command[2]:
        return
    with open(command[1], "r") as old_file, open(command[2], "w") as new_file:
        new_file.write(old_file.read())
