def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command. Usage: cp original_file copied_file")
        return

    original_file, copied_file = parts[1], parts[2]

    if original_file == copied_file:
        print("Original and copied file names"
              " are the same. Nothing to copy.")
        return

    try:
        with (open(original_file, "r") as file_in,
              open(copied_file, "w") as file_out):
            file_out.write(file_in.read())

        print(f"File \"{original_file}\" copied to"
              f" \"{copied_file}\" successfully.")

    except FileNotFoundError:
        print(f"Error: \"{original_file}\" not found.")


# example of usage
copy_file("cp test.txt new_file.txt")
if open("test.txt").read() == open("new_file.txt").read():
    print(True)
else:
    print(False)
