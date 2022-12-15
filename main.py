# write your code here
def copy_file(command: str) -> None:
    commands = command.split()
    first_name, second_name = commands[1], commands[2]

    if first_name != second_name:

        with open(first_name, "r") as file_in, \
                open(second_name, "w") as file_out:
            file_out.write(file_in.read())
