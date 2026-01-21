import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format.")
        return

    source_file = parts[1]
    dest_file = parts[2]
    if source_file == dest_file:
        print("No action taken.")
        return

    try:
        with (open(source_file, "rb") as file_in,
              open(dest_file, "wb") as file_out):
            file_out.write(file_in.read())
        print(f"File '{source_file}' successfully copied to '{dest_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    with open("file.txt", "wb") as f:
        f.write("This is the content of file.txt.\n It has multiple lines.")

    copy_file("cp file.txt file.txt")
    copy_file("cp file.txt new_file.txt")
    if os.path.exists("new_file.txt"):
        with open("file.txt", "rb") as f1, open("new_file.txt", "rb") as f2:
            print(
                f"Content of file.txt equals new_file.txt: "
                f"{f1.read() == f2.read()}"
            )

    copy_file("cp non_existent.txt error_file.txt")
    copy_file("cp file.txt new_file.txt extra_argument")
