def copy_file(command):
    command_data = command.split(' ')
    if command_data[1] != command_data[2]:
        with open(f'{command_data[1]}', 'r') as f:
            with open(f'{command_data[2]}', 'w') as fc:
                fc.write(f.read())


if __name__ == '__main__':
    copy_file('cp file.txt new_file.txt')
