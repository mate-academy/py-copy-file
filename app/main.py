def copy_file(command: str) -> None:
    parts: list = command.split(maxsplit=2)

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file: str = parts[1]
    target_file: str = parts[2]

    if source_file == target_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(target_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"No {source_file} was found...")
    except IOError as e:
        print(f"I/O error! {e}")
