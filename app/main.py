def copy_file(command: str) -> None:
    text = command.split(" ")
    if "cp" not in text[0] or len(text) != 3:
        print("Invalid command. Usage: cp {from_file} {to_file}")
        return
    from_file = text[1]
    to_file = text[2]
    if from_file == to_file:
        return
    with open(from_file, "r") as file_in, open(to_file, "w") as file_out:
        file_out.write(file_in.read())
