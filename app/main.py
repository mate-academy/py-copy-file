# write your code here
def copy_file(command: str) -> None:
    command, original_file, copied_file = command.split(" ")
    if command == "cd" or original_file != copy_file:
        with (open(original_file, "r") as original,
              open(copied_file, "w") as copy):
            copy.write(original.read())
