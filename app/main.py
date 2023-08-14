def copy_file(command: str) -> None:
    arguments = command.split(" ")

    if len(arguments) > 0 and arguments[0] == "cp":
        if len(arguments) < 2:
            print("Missing file operand")

        if len(arguments) < 3:
            print(f"Missing destination file operand after '{arguments[1]}'")

        if arguments[1] == arguments[2]:
            print(f"'{arguments[1]}' and '{arguments[2]}' are the same file")

        try:
            with open(arguments[1], "r") as file_in:
                text = file_in.read()

            with open(arguments[2], "w") as file_out:
                file_out.write(text)

        except FileNotFoundError as e:
            print(e)
        else:
            print("Copy successfully")
    else:
        print("Command not found")


copy_file("cp text1.txt text.txt")