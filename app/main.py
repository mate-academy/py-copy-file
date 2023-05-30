def copy_file(command: str) -> None:
    try:
        command, file, copy = command.split()
    except ValueError:
        raise ValueError(
            'Please use the command: "cp :source_file: :input file:"'
        )
    if file != copy and command == "cp":
        with open(file, "r") as file_in, open(copy, "w") as file_out:
            file_out.write(file_in.read())
