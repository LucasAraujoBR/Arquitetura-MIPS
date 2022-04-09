from mnemonicos import register_base
class RegistersBase:
    # Class Variable


    @staticmethod
    def alter_dicionario(dicionario, registrador, valor):
        register_base = {
            "$0": 0,
            "$1": 0,
            "$2": 0,
            "$3": 0,
            "$4": 0,
            "$5": 0,
            "$6": 0,
            "$7": 0,
            "$8": 0,
            "$9": 0,
            "$10": 0,
            "$11": 0,
            "$12": 0,
            "$13": 0,
            "$14": 0,
            "$15": 0,
            "$16": 8,
            "$17": 12,
            "$18": 0,
            "$19": 0,
            "$20": 0,
            "$21": 0,
            "$22": 0,
            "$23": 0,
            "$24": 0,
            "$25": 0,
            "$26": 0,
            "$27": 0,
            "$28": 268468224,
            "$29": 2147479548,
            "$30": 0,
            "$31": 0,
            "pc": 4194308,
            "hi": 0,
            "lo": 0
        }

        dicionario[registrador] = valor
        return dicionario





