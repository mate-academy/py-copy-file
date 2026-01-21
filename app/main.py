def copy_file(command: str) -> None:
    parts = command.split()
    conditions = (
        len(parts) == 3,
        parts[0] == "cp",
        parts[2] != parts[1]
    )
    if all(conditions):

        with (open(parts[1], "r") as file_in,
              open(parts[2], "w") as file_out):
            file_out.write(file_in.read())
