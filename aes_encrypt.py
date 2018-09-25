def key_expansion():
    pass

def sub_bytes(state):
    pass

def shift_rows(state):
    pass

def mix_columns(state):
    pass

def add_round_key(state, roundkey):
    pass

def aes_encrypt(message, key):
    state = []
    for i in range(16):
        state[i] = message[i]

    num_rounds = 1
    key_expansion()
    add_round_key()

    for i in range(num_rounds):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, key)

    # final round
    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, key)

def main():
    print("I am in Main")
    message = ""
    key = []
    aes_encrypt(message, key)


if __name__ == '__main__':
    main()