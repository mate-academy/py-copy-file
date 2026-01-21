def copy_file(command: str) -> None:
    # Split the command into arguments
    args = command.split()

    if len(args) != 3 or args[0] != "cp":
        print("Invalid command. "
              "Please use the format: cp source_file destination_file")
        return

    source_file = args[1]
    destination_file = args[2]

    if source_file == destination_file:
        print("Cannot copy the file to a file with the same name.")
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"File {source_file} successfully copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: File {source_file} not found.")
    except Exception as e:
        print(f"An error occurred while copying the file: {e}")
