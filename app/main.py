def copy_file(command: str) -> None:
    text = command.split()
    cp, from_file, to_file = text
    if "cp" not in cp or len(text) != 3:
        print("Invalid command. Usage: cp {from_file} {to_file}")
        return
    if from_file == to_file:
        return
    with open(from_file, "r") as file_in, open(to_file, "w") as file_out:
        file_out.write(file_in.read())
