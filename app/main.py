def coopy_file(command: str) -> None:
    elements = command.split()

    if len(elements) < 3 and elements[1] != "cp":
        print("Invalid command. Usage: cp source.file destination.file")

    source_file, destination_file = elements[1], elements[2]

    if source_file != destination_file:
        with open(source_file, "r") as file_in, open(destination_file,
                                                     "w") as file_out:
            file_out.write(file_in.read())
            print(f"File {file_in} copied to {file_out}."
                  f" Successfully")
