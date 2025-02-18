def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        com, file_origin, cp_file = parts
        if file_origin != cp_file and com == "cp":
            with (open(file_origin, "r") as file_in,
                  open(cp_file, "w") as file_out):
                file_out.write(file_in.read())


copy_file("cp file new_file")
