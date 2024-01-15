def copy_file(command: str) -> None:
    cp_command, source_file, destination_file = command.split()

    if cp_command == "cp" and source_file != destination_file:
        with (open(source_file, "r") as file_in, open(destination_file, "w")
                as file_out):
            file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
