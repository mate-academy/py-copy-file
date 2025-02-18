def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        operation, source_file, destination_file = command.split()
        if operation == "cp":
            if source_file != destination_file:
                try:
                    with open(source_file, "r") as file_in,\
                         open(destination_file, "w") as file_out:
                        file_out.write(file_in.read())
                    print(f"File '{source_file}'"
                          f"copied to '{destination_file}'")
                except FileNotFoundError:
                    print(f"Error: File '{source_file}' not found.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Error: Source and destination file names are the same.")
        else:
            print("Error. Operation should be 'cp'")
    else:
        print("Error: Invalid command format."
              "Please use 'cp source_file destination_file'.")
