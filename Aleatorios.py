import nacl.utils, sys

def genRandStr(x):
    randStr = ""
    rand = nacl.utils.random(x)
    
    for e in rand:
        randStr += (hex(e)[2:]).upper()

    return randStr

if __name__ == '__main__':
    x = int(sys.argv[1])
    randStr= genRandStr(x)
    print(f"\nNumero aleatorio de {x} bytes\n-----------------------------------")
    print(f"{randStr}\n")
