def copy_file(names: str) -> None:
    command, old_file, new_file = names.split(" ")
    if command == "cp":
        if not old_file == new_file:
            with (open(old_file, "r") as file_in,
                  open(new_file, "w+") as file_out):
                file_out.write(file_in.read())
