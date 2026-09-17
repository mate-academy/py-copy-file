def copy_file(command: str) -> None:
    try:
        [comm, file_name, new_file_name] = command.split(" ")

        if comm == "cp":
            if file_name != new_file_name:
                with (open(file_name, "r") as file_in,
                      open(new_file_name, "w") as file_out):
                    for line in file_in:
                        file_out.write(line)

    except FileNotFoundError:
        print("File not found")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    copy_file("invalid_command file.txt new_file.txt")
