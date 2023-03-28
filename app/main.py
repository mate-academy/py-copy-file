def copy_file(command: str) -> None:
    parameters = command.split()

    if (len(parameters) == 3
            and parameters[0] == "cp"
            and parameters[1] != parameters[2]):
        new_file = parameters[2]
        old_file = parameters[1]

        with (open(old_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
