def copy_file(command: str) -> None:
    list_command = command.split()
    if len(list_command) == 3 and list_command[0] == "cp":
        cp, source_file_name, destination_file_name = list_command
        if source_file_name != destination_file_name:
            try:
                with (
                    open(source_file_name, "r") as file_in,
                    open(destination_file_name, "w") as file_out
                ):
                    content = file_in.read()
                    file_out.write(content)
            except FileNotFoundError:
                return
