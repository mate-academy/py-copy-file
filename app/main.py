# write your code here
def copy_file(command: str) -> None:
    try:
        command_cp, file_name, file_copy_name = command.split()
    except ValueError:
        raise ValueError(
            "Check if the command has the format: cp file.txt file_copy.txt"
        )
    if command_cp != "cp":
        raise ValueError("The command must start with 'cp'")
    if file_name == file_copy_name:
        raise ValueError("The file copy must have different name")
    with open(file_name, "r") as file_in, \
            open(file_copy_name, "w") as file_out:
        file_out.write(file_in.read())
