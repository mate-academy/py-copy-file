def copy_file(command: str) -> None:
    copy, file_name, new_file_name = command.split()[1:]
    if copy != "cp":
        raise AttributeError(f"Name of copy command "
                             f"should be 'cp', not {copy}")

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        temp = file_in.read()
        file_out.write(temp)
        file_in.close()
        file_out.close()
