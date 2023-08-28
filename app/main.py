def copy_file(command: str) -> None:
    try:
        cp_command, previous_name, new_name = command.split()
    except ValueError:
        raise Exception("Enter correct command!")

    if previous_name != new_name and cp_command == "cp":
        with (
            open(previous_name, "r") as file_in,
            open(new_name, "w") as file_out
        ):
            file_content = file_in.readlines()
            file_out.writelines(file_content)
