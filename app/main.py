def copy_file(command: str) -> None:
    name_file = command.split(" ")
    print(command)
    if name_file[1] != name_file[2] and name_file[0] == "cp":
        with (open(f"{name_file[1]}", "r") as file_in,
              open(f"{name_file[2]}", "w") as file_out):
            file_out.write(file_in.read())
