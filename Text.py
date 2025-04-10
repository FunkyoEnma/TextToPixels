def ascii_a_binario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)