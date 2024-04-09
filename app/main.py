def copy_file(command: str) -> None:
    if (len(command.split()) == 3
            and command.split()[0] == "cp"
            and command.split()[1] != command.split()[2]):
        file_in, file_out = command.split()[1], command.split()[2]
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            file_out.write(file_in.read())
