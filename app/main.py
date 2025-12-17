def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cmd, source_file_name, destination_file_name = parts
    if cmd != "cp":
        return

    if source_file_name == destination_file_name:
        return

    try:
        with (open(source_file_name, "r") as f_in,
              open(destination_file_name, "w") as f_out):
            f_out.write(f_in.read())

    except FileNotFoundError:
        pass

    except Exception:
        pass
