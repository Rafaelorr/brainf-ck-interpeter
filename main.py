import threading

filename :str = input("bestandnaam van de code: ")
pointer :int = 0
data_list :list[int] = [0] * 100
loop :list = []

def error_handeling(filename:str) -> None:
  try:
      with open(filename) as file:
          file.close()
  except FileNotFoundError:
      print("bestand niet gevonden")

def main(pointer:int, filename:str, data_list :list, loop :list) -> None:
  error_handeling(filename)
  with open(filename) as file:
      letter :int = 0
      code :list[str] = file.read().splitlines()
      while letter != len(code) + 1:
          if code[letter] == ">":
              # voeg 1 toe aan de pointer met 1
              pointer += 1
              if pointer == len(data_list):
                  data_list.append(0)
          elif code[letter] == "<":
              # verminder de pointer met 1
              pointer -= 1
              if pointer < 0:
                  data_list.insert(0,0)
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
          elif code[letter] == ",":
              # input int command
              int_input :int = int(input("input int: "))
              data_list[pointer] = int_input
          elif code[letter] == ".":
              # output command
              print(chr(data_list[pointer]))
          elif code[letter] == "/":
              # clear command
              data_list = [0] * len(data_list)
          else:
              continue
          letter + 1
      print(data_list)
      return

error_handel_thread :threading.Thread = threading.Thread(target=error_handeling, args=[filename])
main_thread :threading.Thread = threading.Thread(target=main,args=[pointer,filename,data_list,loop])

error_handel_thread.start()
main_thread.start()