def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command or missing arguments")
        return

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        print(f"Cannot copy the file to itself! "
              f"Source file {source_file} is the same"
              f" as the destination file {destination_file}.")

        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
