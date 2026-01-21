def copy_file(command: str) -> None:
    try:
        copy_command, file, file_copy = command.split(" ")
        if copy_command == "cp" and file != file_copy:
            with open(file, "r") as file_in, open(file_copy, "w") as file_out:
                file_out.write(file_in.read())

    except FileNotFoundError:
        pass
    except ValueError:
        pass
