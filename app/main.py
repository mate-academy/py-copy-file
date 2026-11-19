def copy_file(command: str) -> None:
    try:
        command_str, file_name, new_file_name = command.split(" ")
        if file_name != new_file_name and command_str == "cp":
            with (open(file_name, "rb") as file,
                  open(new_file_name, "wb") as new_file):
                content = file.read()
                new_file.write(content)
    except ValueError:
        pass
    except FileNotFoundError:
        pass