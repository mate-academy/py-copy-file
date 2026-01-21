def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        com_word, file_name, new_file_name = command.split()
        if file_name != new_file_name and com_word == "cp":
            try:
                open(file_name, "r")
            except FileNotFoundError:
                pass
            else:
                with (open(file_name, "r") as file_in,
                      open(new_file_name, "w") as file_out):
                    content = file_in.read()
                    file_out.write(content)
