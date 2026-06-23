def copy_file(command: str) -> None:
    try:
        parts = command.strip().split()
        if len(parts) != 3:
            return None

        cmd, source, destination = parts

        if cmd.lower() != "cp" or source == destination:
            return None

        with open(source, "r") as file_in, open(destination, "w") as file_out:
            for line in file_in:
                file_out.write(line)

    except FileNotFoundError:
        return None
