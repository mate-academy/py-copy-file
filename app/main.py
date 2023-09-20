def copy_file(command: str) -> None:
    cp, input_name, output_name = command.split(" ")
    if input_name == output_name or cp != "cp":
        return
    with open(input_name, "r") as file_in, open(output_name, "w") as file_out:
        file_out.write(file_in.read())
