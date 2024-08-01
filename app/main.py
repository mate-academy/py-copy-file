def copy_file(command: str) -> None:
    command_args = command.split()

    if len(command_args) != 3:
        print("Command must have only three arguments!")

    if command_args[1] != command_args[2]:
        _, source_file, new_file = command_args
        with open(source_file) as file_out, open(new_file, "w") as file_in:
            file_in.writelines(file_out.readlines())
