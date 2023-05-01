# write your code here
def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) < 3 or split_command[1] == split_command[2]:
        return
    else:
        with open(
                split_command[1], "r"
        ) as file_in, open(
            split_command[2], "w"
        ) as file_out:
            file_content = file_in.read()
            file_out.write(file_content)
