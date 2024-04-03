import shutil


def copy_file(command: str) -> None:
    # Split the command string into its components
    parts = command.split()

    # Validate if the command is correct and the number of arguments is correct
    if len(parts) != 3 or parts[0] != "cp":
        print(
            "Invalid command format or command. "
            "Please provide command in the format: cp old_file new_file"
        )
        return

    _, old_file, new_file = parts

    # Validate if the source and destination filenames are the same
    if old_file == new_file:
        print(
            "The source and destination filenames are the same. "
            "Nothing to do."
        )
        return

    try:
        # Copy the file using shutil
        shutil.copy(old_file, new_file)
        print(f"File '{old_file}' copied to '{new_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{old_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
