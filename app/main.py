def copy_file(command: str) -> None:
    input_command, file_name_to_copy, new_file_name = command.split()
    if input_command != "cp":
        return

    with open(file_name_to_copy, "r") as file_in,\
            open(new_file_name, "w") as file_out:
        read_content = file_in.read()
        file_out.write(read_content)


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
