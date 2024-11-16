import os

filename :str = input("bestandnaam van de code: ")
pointer :int = 0
data_list :list[int] = [0] * 100

def error_handeling(filename:str) -> None:
  try:
      with open(filename) as file:
          file.close()
          print("bestand gevonden")
  except FileNotFoundError:
      print("bestand niet gevonden")

def main(pointer:int, filename:str, data_list :list) -> None:
  with open(filename) as file:
      letter :int = 0
      code :list[str] = file.read().splitlines()
      while letter != len(code) + 1:
          
          # pointer functies
          if code[letter] == ">":
              # voeg 1 toe aan de pointer
              pointer += 1
              if pointer == len(data_list):
                  data_list.append(0)
          elif code[letter] == "<":
              # verminder de pointer met 1
              pointer -= 1
              if pointer < 0:
                  data_list.insert(0,0)

          # reken functies
          elif code[letter] == "+":
              # voeg 1 toe aan de huidige cel
              data_list[pointer] += 1
              if data_list[pointer] == 256:
                  data_list[pointer] = 0
          elif code[letter] == "-":
              # verminder de huidige cel met 1
              data_list[pointer] -= 1
              if data_list[pointer] == 0:
                  data_list[pointer] = 255
          elif code[letter] == "*":
              # vermenigvuldig het getal op en voor de pointer met elkaar
              data_list[pointer] = data_list[pointer -1] * data_list[pointer]
          elif code[letter] == "/":
              # deel het getal op en voor de pointer met elkaar
              # het deeltal is het getal voor de pointer
              # de deler is het getal op de pointer
              data_list[pointer] = data_list[pointer -1] / data_list[pointer]

          # andere commands
          elif code[letter] == ",":
              # input int command
              int_input :int = int(input("input int: "))
              data_list[pointer] = int_input
          elif code[letter] == ".":
              # output command
              print(chr(data_list[pointer]))
          elif code[letter] == "µ":
              # clear data command
              data_list :int = [0] * len(data_list)
          elif code[letter] == ";":
              # clear screen command
              os.system('cls' if os.name == 'nt' else 'clear')
          elif code[letter] == "&":
              # jump de waard van de cel voorwaarsts
              pointer += data_list[pointer]
              while pointer > len(data_list):
                  pointer -= 1
          elif code[letter] == "!":
              # jump de waard van de cel achterwaartst
              pointer -= data_list[pointer]
              while pointer < 0:
                  pointer += 1

          else:
              continue
          letter + 1
      print(data_list)
      return

error_handeling(filename)
main(pointer,filename,data_list)