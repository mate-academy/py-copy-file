# write your code here
def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == "cp":
        with open(command[1], "r") as file_in, \
                open(command[2], "w") as file_out:
            result = file_in.read()
            file_out.write(result)
