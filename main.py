filename :str = input("bestandnaam van de code: ")
max_index :int = 100
pointer :int = 0
data_list :list[int] = [0] * max_index


def main(pointer:int, filename:str, max_index:int, data_list :list) -> None:
    # error handeling
    try:
        with open(filename) as file:
            file.close()
    except FileNotFoundError:
        print("bestand niet gevonden")

    with open(filename) as file:
        while True:
            letter:str = file.read(1)
            if not letter:
                print(data_list)
                break
            if letter == ">" and not pointer == max_index - 1:
                pointer += 1
            elif letter == "<" and not pointer == 0:
                pointer -= 1
            elif letter == "+":
                data_list[pointer] += 1
            elif letter == "-" and not data_list[pointer] == 0:
                data_list[pointer] -= 1
            elif letter == ",":
                int_input :int = int(input("input int: "))
                data_list[pointer] = int_input
            elif letter == ".":
                print(chr(data_list[pointer]))
            else:
                continue
        return

main(pointer,filename,max_index,data_list)