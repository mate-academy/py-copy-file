
def copy_file(command: str) -> None:
    new_str = command.split()

    file_first = new_str[1]
    file_second = new_str[2]
    cmd = new_str[0]

    if file_first != file_second and cmd == "cp" and len(new_str) == 3:

        try:
            with (
                open(file_first, "r") as first,
                open(file_second, "w") as second
            ):
                for line in first:
                    second.write(f"{line}")
        except OSError as e:
            print(f"Error {e}")


