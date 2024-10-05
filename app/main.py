def copy_file(command: str) -> None:
    data = command.split()
    if len(data) != 3 and data[0].lower() == "cp":
        raise "Invalid command format. Correct: cp <source_file> <target_file>"
    source_file, target_file = data[1], data[2]
    if source_file == target_file:
        return print("Does nothing")
    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
