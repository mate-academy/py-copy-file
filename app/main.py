def copy_file(command: str) -> None:
    command, source_file, destination_file = command.split()

    if source_file == destination_file or command != "cp":
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.writelines(file_in.readlines())
    except FileNotFoundError:
        print(f"No {source_file} was found...")
    except IOError as e:
        print(f"I/O error! {e}")
