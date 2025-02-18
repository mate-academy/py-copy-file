def copy_file(command: str) -> None:
    command, source, destination = command.split()
    if source == destination:
        print("you can not create files with simular names")
    else:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
