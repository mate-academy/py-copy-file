def copy_file(command: str) -> None:
    cp, file_name, new_file_name = command.split()
    if cp != "cp":
        raise ValueError(f"Command not found: {cp}")
    if file_name == new_file_name:
        return None

    with (open(file_name, "r") as file_in,
          open(new_file_name, "w") as file_out):
        file_out.writelines(file_in.readlines())
