def copy_file(string: str) -> None:
    parts = string.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Invalid command. Use 'cp <source> <destination>' format."
        )

    source_file = parts[1]
    destination_file = parts[2]
    if source_file == destination_file:
        print("Source and destination files are the same. No action taken.")
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
