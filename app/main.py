def copy_file(text: str) -> None:
    if len(text.split()) == 3:
        cp, in_file, out_file = text.split()
        if cp == "cp" and in_file != out_file:
            with (open(in_file, "r") as file_in,
                  open(out_file, "w") as file_out):
                file_out.write(file_in.read())
