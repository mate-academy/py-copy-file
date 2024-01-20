def copy_file(command: str) -> None:
    instruction, f_in_name, f_out_name = command.split()
    if instruction != "cp" or f_in_name == f_out_name:
        return

    with open(f_in_name, "r") as file_in, open(f_out_name, "w") as file_out:
        file_out.write(file_in.read())
