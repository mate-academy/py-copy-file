import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        _, old_file, new_file = parts

        if old_file == new_file:
            print(
                "The source and destination filenames are the same. "
                "Nothing to do."
            )
        else:
            try:
                shutil.copy(old_file, new_file)
            except FileNotFoundError:
                print(f"Error: File '{old_file}' not found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
    else:
        print(
            "Invalid command format or command. "
            "Please provide command in the format: cp old_file new_file"
        )
