def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) == 3 or command.startswith("cp "):
        _, file_name_in, file_name_out = command_list

        if file_name_in != file_name_out:
            try:
                with (open(file_name_in) as file_in,
                      open(file_name_out, "w") as file_out):
                    file_out.write(file_in.read())
            except (FileNotFoundError, PermissionError) as e:
                raise f"Error {e}. The file does not exist or can not be read"
