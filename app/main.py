
def copy_file(command: str) -> None:
    splited_command = command.split(" ")
    if splited_command[0].lower() == "cp":
        if splited_command[1] != splited_command[2]:
            with (open(splited_command[1], "r") as file_in,
                open(splited_command[2], "w") as file_out):
                file_in_text = file_in.read()
                file_out.write(file_in_text)

