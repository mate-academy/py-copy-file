def copy_file(command: str):
    command = command.split()
    if command[0] == 'cp' and command[1] != command[2]:
        with open(command[1], mode='r') as file_in:
            with open(command[2], mode='w') as file_out:
                for line in file_in:
                    file_out.write(line)


if __name__ == "__main__":
    copy_file("cp file.txt file1.txt")
