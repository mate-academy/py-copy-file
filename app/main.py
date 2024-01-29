def copy_file(command: str) -> None:
    args = command.split()
    source_file, destination_file = args[1], args[2]

    if source_file == destination_file:
        print("Source and destination files are the same.")
    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    finally:
        file_in.close()
        file_out.close()
