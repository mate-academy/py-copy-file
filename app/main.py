def copy_file(command: str) -> list:
    result = command.split()
    with open(result[1], "r") as file_in, open(result[2], "w") as file_out:
        if result[1] == result[2]:
            return []
        result = file_in.read()
        file_out.write(result)


copy_file("cp file.txt file2.txt")
