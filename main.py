# William St. Peter Lab 06 Software Engineering
def encode(password):
    listed_password = list(password)
    encoded_password_list = [str(int(a) + 3) for a in listed_password]
    password = "".join(encoded_password_list)
    print(password)
    return password


def main():
    option = 0

    while option != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter a password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        if option == 2:
            print("NO WRITTEN FUNCTION YET")
        if option == 3:
            break


if __name__ == "__main__":
    main()
