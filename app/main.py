def copy_file(command: str) -> None:
    components = command.split()
    if len(components) == 3 and components[0] == "cp":
        file_in, file_out = components[1], components[2]
    else:
        print("Invalid command")
        return

    if components[1] == components[2]:
        print("No action to be taken")
        return

    with (
        open(file_in, "r") as source_file,
        open(file_out, "w") as destination_file
    ):
        destination_file.write(source_file.read())


if __name__ == '__main__':
    copy_file("cp file.txt file-copy.txt")
