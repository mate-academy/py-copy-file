import shutil


def copy_file(command: str) -> None:
    try:
        command, file_name_to_copy, new_file_name = command.split()

        if command == "cp" and file_name_to_copy != new_file_name:
            with open(f"{file_name_to_copy}", "r") as file_name_to_copy:
                shutil.copyfile(
                    f"{file_name_to_copy.name}",
                    f"{new_file_name}"
                )

    except FileNotFoundError:
        pass
    except ValueError:
        pass
