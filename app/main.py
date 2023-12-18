def copy_file(command: str) -> None:
    splitted_arguments = command.split()
    if len(splitted_arguments) != 3:
        raise ValueError("Incorrect command provided")
    command, fname_to_copy, new_fname = splitted_arguments

    if command != "cp" or fname_to_copy == new_fname:
        raise ValueError("Incorrect command provided")

    with open(fname_to_copy, "r") as file_in, open(new_fname, "w") as file_out:
        file_out.write(file_in.read())
