CODES = ['wink', 'double blink', 'close your eyes', 'jump']


def handshake(code):
    code_bin = format(code, 'b')[::-1]
    reverse = False
    if len(code_bin) > 4:
        reverse = True
        code_bin = code_bin[0:4]
    secret_handshake = [CODES[ind] for ind, val in enumerate(code_bin) if val == '1']
    if reverse:
        secret_handshake.reverse()

    return secret_handshake


def secret_code(actions):
    pass
