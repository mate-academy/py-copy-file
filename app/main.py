# write your code here
def copy_file(command: str) -> None:
    command = command.split(" ")
    if command[0] != "cd" or command[1] == command[2]:
        return
    with open(command[1], "r") as original, open(command[2], "w") as copy:
        copy.write(original.read())
