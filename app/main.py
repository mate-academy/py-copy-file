def copy_file(command: str) -> None:
    try:
        comm, source_file, destination_file = command.split()
        if comm == "cp" and source_file != destination_file:
            try:
                with (open(source_file) as file_in,
                      open(destination_file, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print("No such file or directory, create file.")
    except ValueError:
        print("Enter 3 elements: command, source file and destination file.")
