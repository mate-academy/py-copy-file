# write your code here
def copy_file(command: str) -> None:
    command, original_file, copy_file = command.split(" ")
    if command == "cd" or original_file != copy_file:
        with open(original_file, "r") as original, open(copy_file, "w") as copy:
            copy.write(original.read())
