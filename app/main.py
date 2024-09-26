def copy_file(command: str) -> None:
    cp, sours_fl, new_fl = command.split()
    if sours_fl != new_fl and cp == "cp":
        with open(sours_fl, "r") as file_in, open(new_fl, "w") as file_out:
            file_out.write(file_in.read())
