
def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    dir_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down

        rail[row][col] = char
        col += 1

        row += 1 if dir_down else -1

    result = ''
    for r in rail:
        result += ''.join([c for c in r if c != '\n'])
    return result


def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    dir_down = None
    row, col = 0, 0

    # Mark the rail pattern
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        row += 1 if dir_down else -1

    # Fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the matrix in zig-zag
    result = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        result += rail[row][col]
        col += 1

        row += 1 if dir_down else -1

    return result


# Example
message = "WEAREDISCOVEREDFLEEATONCE"
key = 3

encrypted = rail_fence_encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = rail_fence_decrypt(encrypted, key)
print("Decrypted:", decrypted)
