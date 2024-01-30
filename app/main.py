def copy_file(command: str) -> None:
    parts = command.split()

    if not command.startswith("cp "):
        print("Invalid command."
              "Please provide a command in the format: "
              "cp source_file destination_file")
        return

    _, source_file, destination_file = parts

    if source_file == destination_file:
        raise Exception("Source and destination file names are the same. "
                        "Nothing will be done.")

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_content = file_in.read()
        file_out.write(file_content)

        print(f"File '{source_file}' copied to "
              f"'{destination_file}' successfully.")
