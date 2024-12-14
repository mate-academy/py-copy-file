def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    source_file = parts[1]
    dest_file = parts[2]

    if source_file == dest_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(dest_file, "w") as file_out):
            for line in file_in:
                file_out.write(line)
            print(f"File copied from {source_file} to {dest_file}")
    except FileNotFoundError:
        print(f"File {source_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
