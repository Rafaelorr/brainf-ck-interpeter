filename :str = input("bestandnaam van de code: ")
pointer :int = 0
data_list :list[int] = [0] * 100
loop :list = []

def main(pointer:int, filename:str, data_list :list, loop :list) -> None:
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
          if letter == ">":
              # voeg 1 toe aan de pointer met 1
              pointer += 1
              if pointer == len(data_list):
                  data_list.append(0)
          elif letter == "<":
              # verminder de pointer met 1
              pointer -= 1
              if pointer < 0:
                  data_list.insert(0,0)
          elif letter == "+":
              # voeg 1 toe aan de huidige cel
              data_list[pointer] += 1
              if data_list[pointer] == 256:
                  data_list[pointer] = 0
          elif letter == "-":
              # verminder de huidige cel met 1
              data_list[pointer] -= 1
              if data_list[pointer] == 0:
                  data_list[pointer] = 255
          elif letter == ",":
              # input int command
              int_input :int = int(input("input int: "))
              data_list[pointer] = int_input
          elif letter == ".":
              # output command
              print(chr(data_list[pointer]))
          elif letter == "/":
              # clear command
              data_list = [0] * len(data_list)
          else:
              continue
      return

main(pointer,filename,data_list,loop)