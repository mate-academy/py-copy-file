def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    (copy_command, file_original, file_copied) = command_parts
    if copy_command != "cp" or file_original == file_copied:
        return
    try:
        with (
            open(file_original, "r") as fobj_original,
            open(file_copied, "w") as fobj_copied
        ):
            fobj_copied.write(fobj_original.read())
    except FileNotFoundError:
        print(f"Error: file named {file_original} not found.")
    except EnvironmentError as e:
        print(f"Error: {e}. File named {file_original} could not be copied.")
