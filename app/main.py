def copy_file(command: str) -> None:
    temp_list = command.split()
    if temp_list[0] != "cp" or (
            not temp_list[1].endswith(".txt")
            or not temp_list[2].endswith(".txt")
    ):
        print("Invalid command format! "
              "Please, follow this ex: 'cp file.txt file_copy.txt'")
        return
    if temp_list[1] != temp_list[2]:
        with open(temp_list[1], "r") as file_in, open(
                temp_list[2], "w") as file_out:
            temp = file_in.read()
            file_out.write(temp)
