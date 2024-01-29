def copy_file(command: str) -> None:
    var1, var2, var3 = command.split()

    if var2 != var3 and var1 == "cp":
        with (open(var2, "r") as old_file,
              open(var3, "w") as new_file):
            content = old_file.read()
            new_file.write(content)
