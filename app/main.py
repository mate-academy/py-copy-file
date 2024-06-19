def copy_file(command: str) -> None:
    elements = command.split(" ")
    if elements[1] != elements[2]:
        with open(elements[1], "r") as file_out, open(
            elements[2], "w"
        ) as file_in:
            text = file_out.read()
            file_in.write(text)


print("Command format: cp [Name of the source file] [Name of the final file]")
while True:
    command_text = input("Type the command: ")
    if not command_text.startswith("cp"):
        print("Incorrect command name. Try again")
    else:
        try:
            copy_file(command_text)
            break
        except Exception:
            print("Error in command")
            continue
