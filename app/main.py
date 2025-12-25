def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("We need 3 elements!")
    cp_command, file, new_file = command.split()
    if cp_command != "cp":
        raise ValueError(f"The first argument must be 'cp'! "
                         f"Instead '{cp_command}' provided.")

    if file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
