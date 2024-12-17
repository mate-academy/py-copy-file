def copy_file(command: str) -> None:
    copy_data = command.split()

    if len(copy_data) == 3 and copy_data[0] == "cp":
        cp_command, file_to_copy_name, new_file_name = copy_data

        if file_to_copy_name != new_file_name:
            with (open(file_to_copy_name, "r") as file_in,
                open(new_file_name, "w") as file_out):
                for line in file_in:
                    file_out.write(f"{line}")
