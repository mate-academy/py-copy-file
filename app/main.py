def copy_file(command: str) -> None:
    copy, file_name, new_file_name = command.split()
    if copy != "cp":
        raise AttributeError(f"Name of copy command "
                             f"should be 'cp', not {copy}")

    if file_name == new_file_name:
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
        file_in.close()
        file_out.close()
