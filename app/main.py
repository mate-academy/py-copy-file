
def copy_file(command: str) -> str | None:
    new_str = command.split()
    if len(new_str) < 3:
        return "argument is not correct"
    file_first = new_str[1]
    file_second = new_str[2]
    cmd = new_str[0]
    if cmd != "cp":
        return "Command is not correct"

    if file_first == file_second:
        pass
    else:
        try:
            with (
                open(file_first, "r") as first,
                open(file_second, "w") as second
            ):
                for line in first:
                    second.write(f"{line}")
        except OSError as e:
            print(f"Error {e}")


copy_file("cp file.txt new_file.txt")
