def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        source_file, copied_file = parts[1], parts[2]

        if source_file != copied_file:
            with (
                open(source_file, "r") as read_file,
                open(copied_file, "w") as write_file,
            ):
                write_file.write(read_file.read())


if __name__ == "__main__":
    copy_file("cp test.txt new_test.txt")
