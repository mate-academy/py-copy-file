def copy_file(command: str) -> None:
    parts = command.split()
    if (len(parts) == 3
            and parts[0] == "cp"
            and parts[1] != parts[2]):
        file_in, file_out = parts[1], parts[2]
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            file_out.write(file_in.read())
