def copy_file(command: str) -> None:
    try:
        command_type, source_file, target_file = command.split()
    except ValueError:
        return

    if command_type != "cp" or source_file == target_file:
        return

    try:
        with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"No {source_file} was found...")
    except IOError as e:
        print(f"I/O error! {e}")
