try:
    with open('not_existing_file.txt') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print('Error : FileNotFoundError')

except :
    print('Unknown Error')

print('Hello World')