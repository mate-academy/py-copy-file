def copy_file(command: str) -> str:
    old_file, new_file = command.split()[1:]
    if old_file == new_file:
        return f"The file '{old_file}' already exists with the same name"

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

    return f"cp {old_file} new_{new_file}"
