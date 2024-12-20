import os
import sys

try:
  filename :str = sys.argv[1]
except IndexError:
  print("geef een filenaam")
  exit(1)
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
  with open(filename,"r") as file:
    for line in file:
       for word in line.split():
          # pointer functies
          if word == ">":
            # voeg 1 toe aan de pointer
            pointer += 1
            if pointer == len(data_list):
              data_list.append(0)
          elif word == "<":
            # verminder de pointer met 1
            pointer -= 1
            if pointer < 0:
              data_list.insert(0,0)
          # reken functies
          elif word == "+":
            # voeg 1 toe aan de huidige cel
            data_list[pointer] += 1
            if data_list[pointer] == 256:
              data_list[pointer] = 0
          elif word == "-":
            # verminder de huidige cel met 1
            data_list[pointer] -= 1
            if data_list[pointer] == 0:
              data_list[pointer] = 255
          elif word == "*":
            # vermenigvuldig het getal op en voor de pointer met elkaar
            data_list[pointer] = data_list[pointer -1] * data_list[pointer]
          elif word == "/":
            # deel het getal op en voor de pointer met elkaar
            # het deeltal is het getal voor de pointer
            # de deler is het getal op de pointer
            data_list[pointer] = data_list[pointer -1] / data_list[pointer]
          # andere commands
          elif word == ",":
            # input int command
            int_input :int = int(input("input int: "))
            data_list[pointer] = int_input
          elif word == ".":
            # output command
            print(chr(data_list[pointer]))
          elif word == "µ":
            # clear data command
            data_list :int = [0] * len(data_list)
          elif word == ";":
            # clear screen command
            os.system('cls' if os.name == 'nt' else 'clear')
          elif word == "&":
            # jump de waard van de cel voorwaarsts
            pointer += data_list[pointer]
            while pointer > len(data_list):
              pointer -= 1
          elif word == "!":
            # jump de waard van de cel achterwaartst
            pointer -= data_list[pointer]
            while pointer < 0:
              pointer += 1
          else:
            continue
    print(data_list)
    return

error_handeling(filename)
main(pointer,filename,data_list)