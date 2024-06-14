def copy_file(command: str) -> None:
    old_file, new_file = command.split(" ")[1], command.split(" ")[2]
    if new_file != old_file:
        with open(new_file, "w") as file_in, open(old_file, "r") as file_out:
            lines = file_out.readlines()
            for line in lines:
                file_in.write(line)

            print(f"all info from {old_file} was copy to {new_file}")


copy_file("cp file.txt new_file.txt")
