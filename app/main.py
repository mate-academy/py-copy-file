def copy_file(command_line: str) -> None:
    command, old_file, new_file = command_line.split()
    content = ""

    if old_file == new_file:
        return

    if command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            # collect all text from old file to variable content
            content += "".join(file_in.readlines())
            file_out.writelines(content)
            print(f"File {old_file} has been copied to the file {new_file}")
