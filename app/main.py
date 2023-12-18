def copy_file(command: str) -> None:
    splitted_arguments = command.split(" ")
    if len(splitted_arguments) != 3:
        raise ValueError("Incorrect comand provided")
    command, fname_to_copy, new_fname = command.split(" ")

    if not command == "cp":
        raise ValueError("Incorrect comand provided")

    if fname_to_copy == new_fname:
        raise ValueError("Incorrect comand provided")

    with open(fname_to_copy, "r") as file_in, open(new_fname, "w") as file_out:
        file_out.write(file_in.read())
