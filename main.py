import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Generate transaction data to deploy any random hex string to Ethereum as smart contract bytecode"
    )

    inputs = parser.add_argument_group("input arguments")
    inputs.add_argument(
        "-b",
        "--bytecode",
        help="hex-encoded bytecode string (60606040...)"
    )
    args = parser.parse_args()

    if not (
        args.bytecode
    ):
        parser.print_help()
        sys.exit(0)

    if args.bytecode:
        deploy_payload = build_deploy_string(hex_string=args.bytecode)
        print(deploy_payload)

def build_deploy_string(hex_string=""):
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]

    hex_string_length = int(len(hex_string) / 2)

    # Init payload
    payload = ""

    # PUSH [hex string length]
    payload += evm_push(hex_string_length)
    # PUSH [offset]
    payload += evm_push(11 + byte_size(hex_string_length) * 2) 
    # PUSH [memory_offset]
    payload += evm_push(0)

    # CODECOPY
    payload += evm_codecopy()

    # PUSH [hex string length]
    payload += evm_push(hex_string_length)
    # PUSH [0]
    payload += evm_push(0)

    # RETURN
    payload += evm_return()

    # Stop execution
    payload += evm_stop()

    # Add the hex string
    payload += hex_string

    return payload

"""
    PUSH1 0 - 2**8-1
    PUSH2 2**8 - 2**16
    ...
    PUSH32 2**255 - 2**256
"""
def evm_push(size=0):
    push_size = byte_size(number=size)

    payload = ""
    payload += str(59 + push_size)
    payload += '{0:0{1}x}'.format(size,(push_size) * 2)
    return payload

"""
    CODECOPY
"""
def evm_codecopy():
    return "39"


"""
    RETURN
"""
def evm_return():
    return "f3"


"""
    STOP
"""
def evm_stop():
    return "00"

"""
    Return the byte size that this number fits in
"""
def byte_size(number=0):
    push_size = 0
    for p in list(range(256, 0, -8)):
        if (int(number / (2 ** p)) > 0):
            push_size = int(p / 8)
            break
    return push_size + 1

if __name__ == "__main__":
    main()
