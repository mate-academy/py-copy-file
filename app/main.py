def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        source_file, destination_file = parts[1], parts[2]
        if source_file != destination_file:
            try:
                with open(source_file, "r") as file_in:
                    content = file_in.read()

                with open(destination_file, "w") as file_out:
                    file_out.write(content)
                print(f"File '{source_file}' copied to '{destination_file}'")
            except FileNotFoundError:
                print(f"Error: File '{source_file}' not found.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Error: Source and destination file names are the same.")
    else:
        print("""Error: Invalid command format.
            Please use 'cp source_file destination_file'.""")
