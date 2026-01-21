def copy_file(command: str) -> None:
    split_name = command.split()
    if len(split_name) != 3:
        return
    if split_name[0] != "cp":
        return
    if split_name[1] != split_name[2]:
        try:
            with (open(split_name[1], "r") as file_in,
                  open(split_name[2], "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print("File not found")
