def copy_file(command: str) -> None:
    cp, initial_file, new_file = command.split()
    if initial_file != new_file and cp == "cp":
        with (open(initial_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in)


if __name__ == "__main__":
    copy_file("cp text.txt text.txt")
