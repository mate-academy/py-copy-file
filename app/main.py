def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command."
              "Please provide a command in the format: "
              "cp source_file destination_file")
        return

    _, source_file, destination_file = parts

    if source_file == destination_file:
        print("Source and destination file names are the same."
              "Nothing will be done.")
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_content = file_in.read()
            file_out.write(file_content)

        print(f"File '{source_file}' copied to "
              f"'{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as error:
        print(f"Error: {error}")
