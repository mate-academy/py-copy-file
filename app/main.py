import os


def copy_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format")
        return

    if not os.path.isfile(source_file):
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except (FileNotFoundError, IOError) as err:
        print("Error: ", err)
