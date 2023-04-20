# write your code here
def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        old_file = command_list[1]
        new_file = command_list[2]
        if old_file != new_file and command_list[0] == "cp":
            with open(old_file, "r") as old, open(new_file, "w") as new:
                new.write(old.read())
