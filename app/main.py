def copy_file(command: str) -> None:
    try:
        cp_command, original_file, copy_file = command.split(" ")
        if cp_command == "cp" and original_file != copy_file:
            with (open(original_file, "r") as file_in,
                    open(copy_file, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
    except ValueError:
        pass
    except FileNotFoundError:
        pass
