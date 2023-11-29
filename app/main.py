def copy_file(command: str) -> None:
    parts = command.split()
    if (parts[0] == "cp"
       and parts[1] != parts[2]
       and len(parts) == 3):
        with (open(parts[1], "r") as file_in,
             open(parts[2], "w") as file_out):
            file_out.write(file_in.read())
