def copy_file(command: str) -> None:
    cp, filename, copy_filename = command.split()
    if cp != "cp" or (
            not filename.endswith(".txt")
            or not copy_filename.endswith(".txt")
    ):
        print("Invalid command format! "
              "Please, follow this ex: 'cp file.txt file_copy.txt'")
        return

    with open(filename, "r") as file_in, open(
            copy_filename, "w") as file_out:
        temp = file_in.read()
        file_out.write(temp)
