def copy_file(command: str) -> None:
    command, fname_to_copy, new_fname = command.split(" ")
    if fname_to_copy == new_fname:
        pass

    with open(fname_to_copy, "r") as file_in, open(new_fname, "w") as file_out:
        file_out.write(file_in.read())
