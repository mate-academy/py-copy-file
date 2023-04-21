# write your code here
def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        cmd, old_file, new_file = command_list
        if old_file != new_file and cmd == "cp":
            with open(old_file, "r") as old, open(new_file, "w") as new:
                new.write(old.read())
