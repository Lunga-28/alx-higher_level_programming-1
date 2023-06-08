#!/usr/bin/python3

import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()

    bytecode = dis.Bytecode(code)

    names = set()
    for instr in bytecode:
        if instr.opname == "LOAD_CONST":
            const = instr.argval
            if isinstance(const, str) and not const.startswith("__"):
                names.add(const)

    for name in sorted(names):
        print(name)
