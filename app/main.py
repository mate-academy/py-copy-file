def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == "cp" and command[1] != command[2]:
        with open(command[1], "r") as file_input:
            with open(command[2], "w") as file_output:
                for line in file_input:
                    file_output.write(line)


if __name__ == "__main__":
    copy_file("cp file.txt file1.txt")
