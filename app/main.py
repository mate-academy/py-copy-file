def copy_file(command: str) -> None:
    command_name, file, file_to_copy = command.split()
    if command_name != "cp":
        print("This command not exist")
        return
    try:
        with (open(file, "r") as current_file,
              open(file_to_copy, "x") as new_file):
            new_file.write(current_file.read())
    except FileNotFoundError:
        print(f"There is not file with name {file}")
        return
    except FileExistsError:
        print("This file already exist")
