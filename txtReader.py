def txt_reader(name = 'a.txt'):
    f = open(name, 'r')
    #pula a linha .config
    f.readline()

    #pega o regs e o mem
    regs = f.readline()
    mem = f.readline()

    #pula o .text
    f.readlines(2)

    #pega a lista de hexadecimal
    hex = [i.rstrip() for i in f.readlines()]

    f.close()
    return regs, mem, hex


regs, mem, hex = txt_reader()
print(regs, mem, hex)