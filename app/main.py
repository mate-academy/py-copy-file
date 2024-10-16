def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format. "
                         "Expected: 'cp file.txt new_file.txt'")

    old_file_name = parts[1]
    new_file_name = parts[2]

    if old_file_name == new_file_name:
        return

    with (open(old_file_name, "r") as file_in,
          open(new_file_name, "w") as file_out):
        file_out.write(file_in.read())


copy_file("cp file.txt new_file.txt")
copy_file("cp file.txt file.txt")


with open("file.txt", "r") as f:
    original_content = f.read()

with open("new_file.txt", "r") as f:
    copied_content = f.read()

print(original_content == copied_content)
