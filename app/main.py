def copy_file(command: str) -> None:
    original_file = "".join(command.split()[-2])
    copied_file = "".join(command.split()[-1])
    if original_file != copied_file:
        with (open(original_file, "r") as file_in,
              open(copied_file, "w") as file_out):
            text = file_in.read()
            file_out.write(text)
