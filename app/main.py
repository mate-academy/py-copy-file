def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    command = command_parts[0]

    if command != "cp":
        return

    source_file = command_parts[1]
    destination_file = command_parts[2]

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.writelines(file_in.readlines())
    except FileNotFoundError:
        print(f"No {source_file} was found...")
    except IOError as e:
        print(f"I/O error! {e}")
