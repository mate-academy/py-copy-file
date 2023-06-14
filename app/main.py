def copy_file(command: str) -> None:
    cmd, file_in, file_out = command.split()
    if not cmd == "cp":
        return
    try:
        with (open(file_in, "r") as file_in,
              open(file_out, "x") as file_out):
            file_out.write(file_in.read())
    except FileExistsError:
        print("File is already exist")
