instructions = ["0x20080000","0x02114020","0x00430820","0x00430822","0x0043082a","0x20410064", "0x3c0d7fff"]

def convert_bin(list_hex):
  list_hex_without_0x = [x.replace("0x","") for x in list_hex]
  list_bins = list()
  for instruction in list_hex_without_0x:
    instruction_bin = ""
    for algarismo in instruction:
        num = bin(int(f"0x{algarismo}",16)).replace("0b","")
        num = "0"*(4-len(num)) + num
        instruction_bin += num
    list_bins.append(instruction_bin)
  return list_bins

# print(convert_bin(instructions))

