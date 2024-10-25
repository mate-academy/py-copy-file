def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        source_file, target_file = parts[1], parts[2]

        if source_file == target_file:
            return

        with (open(source_file, "r") as file_in,
              open(target_file, "w") as file_out):
            file_out.write(file_in.read())
