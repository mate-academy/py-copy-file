from pathlib import Path


def copy_file(command: str) -> None:
    text = command.split(" ")
    error = "Invalid file name"
    if len(text) != 3:
        print(error)
        return
    if text[0] != "cp":
        print(error)
        return

    file_in = text[1]
    file_out = text[2]
    file_path = Path(file_in)
    if not file_path.exists():
        print(f"The file {file_in} does not exist!!!")
        return

    if file_in != file_out:
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            lines = file_in.readlines()
            file_out.writelines(lines)
        print(f"File {file_in} copied in {file_out} successfully!")
    else:
        print("you can't copy a file to itself!!!")
