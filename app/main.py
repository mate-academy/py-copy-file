def copy_file(command: str) -> None:
    cp_command, file, new_file = command.split()
    if cp_command != "cp":
        raise ValueError(f"The first argument must be 'cp'! "
                         f"Instead '{cp_command}' provided.")

    with open(file, "r") as file_in, open(new_file, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
