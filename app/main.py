def copy_file(command: str) -> None:
    command, filename1, filename2 = command.split()

    if filename1 != filename2 and command == "cp":
        try:
            with open(filename1, "r") as file_in, \
                    open(filename2, "w") as file_out:
                file_out.write(file_in.read())
        except FileNotFoundError as e:
            print(e)
