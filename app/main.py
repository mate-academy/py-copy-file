def copy_file(command: str) -> None:
    if command:
        words = command.split()
        if len(words) == 3 and words[0] == "cp":
            file_name_1 = words[1]
            file_name_2 = words[2]
            if file_name_1 != file_name_2:
                try:
                    with open(file_name_1, "r") as file_in, open(file_name_2, "w") as file_out:
                        text = file_in.read()
                        file_out.write(text)
                except:
                    print("Missing source file")
