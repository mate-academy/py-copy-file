def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if command == "cp" and old_file != new_file:
        with (open(old_file, "r") as file_input,
              open(new_file, "w") as file_output):
            for line in file_input:
                file_output.write(line)


if __name__ == "__main__":
    copy_file("cp file.txt file1.txt")
