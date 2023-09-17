def copy_file(command: str):
    data = command.split(" ")
    if data[1] == data[2]:
        return
    else:
        with open(data[1], "r") as file_in, open(data[2], "w") as file_out:
            file_data = file_in.readlines()
            for row in file_data:
                file_out.write(row)


print('try copy the same')
copy_file("cp file.txt file.txt")
print('copy different')
copy_file("cp file.txt new_file.txt")
check = open("file.txt").read() == open("new_file.txt").read()  # True
print(f'check {check}')
