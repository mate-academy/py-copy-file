def copy_file(command: str) -> None:
    components = command.split()
    command_, source_file, destination_file = command.split()

    if len(components) == 3 and command_ == "cp":
        if source_file != destination_file:

            try:

                with (open(source_file, "r") as file_in,
                      open(destination_file, "w") as file_out):

                    file_out.write(file_in.read())
            except FileNotFoundError as e:
                print(e)
