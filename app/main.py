# write your code here
def copy_file(command: str) -> None:
    params = command.split()
    if len(params) == 3:
        command_name, file_name, copy_file_name = params
        if file_name != copy_file_name and command_name == "cp":
            with open(file_name, "r") as file:
                with open(copy_file_name, "w") as new_file:
                    new_file.write(file.read())
