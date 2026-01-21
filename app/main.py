def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format")
        return

    src_file_name = parts[1]
    dest_file_name = parts[2]

    if src_file_name == dest_file_name:
        return

    try:
        with (open(src_file_name, "r") as input_file,
              open(dest_file_name, "w") as output_file):
            output_file.write(input_file.read())
    except FileNotFoundError:
        print(f"File {src_file_name} not found.")
    except Exception as e:
        print(f"An error occured: {e}")
