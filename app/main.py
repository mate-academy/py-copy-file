# write your code here
def copy_file(command: str) -> None:
    spaces = command.count(" ")
    if spaces == 2 and command[:3] == "cp ":
        part_command = command.split(" ")
        old_file = part_command[1]
        new_file = part_command[2]

        if old_file != new_file:
            try:
                with open(old_file, "r") as f, open(new_file, "a") as n:
                    for line in f:
                        n.write(line)
            except FileNotFoundError:
                pass
