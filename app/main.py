def copy_file(command: str) -> None:
    try:
        parts = command.split()
        if len(parts) != 3 or parts[0] != "cp":
            print("Invalid command. Format: cp source_file destination_file")
            return
        source_file, destination_file = parts[1], parts[2]
        if source_file == destination_file:
            print("Cannot copy a file to itself.")
            return
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"File {source_file} successfully copied to {destination_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")
