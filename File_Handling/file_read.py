with open('to_do_list.txt', 'r+') as file:
    contents = file.read()
    # print(contents)
    cap_contents = contents.upper()
    file.seek(0)
    file.write(cap_contents)
    # file.truncate()