# Golubeva Anna ИВТ2
""" ROT13:
 Разработать программу, реализовывающую алгоритм шифрования ROT13.
 Программа должна уметь
       считать текстовую строку из файла/из консоли;
       закодировать/раскодировать строку и отобразить её на экране;
       записать закодированную/раскодированную строку в файл;
  В программе должен использоваться механизм обработки исключений."""


def alphabet():
    first_part_of_encrypt = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S'}
    second_part_of_encrypt = {'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z'}

    first_part_of_decrypt = {'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F'}
    second_part_of_decrypt = {'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    first_part_of_encrypt.update(second_part_of_encrypt)
    first_part_of_decrypt.update(second_part_of_decrypt)
    first_part_of_encrypt.update(first_part_of_decrypt)  # uppercase dictionary

    first_low_part_of_encrypt = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's'}
    second_low_part_of_encrypt = {'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z'}

    first_low_part_of_decrypt = {'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f'}
    second_low_part_of_decrypt = {'t': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

    first_low_part_of_encrypt.update(second_low_part_of_encrypt)
    first_low_part_of_decrypt.update(second_low_part_of_decrypt)
    first_low_part_of_encrypt.update(first_low_part_of_decrypt)  # lowercase dictionary

    first_part_of_encrypt.update(first_low_part_of_encrypt)  # full dictionary

    return first_part_of_encrypt

def ROT13():
    alpha = alphabet()
    print('What do You want to do? \n 1.(ROT13 -> EN) \n 2.(EN -> ROT13)  ')
    x = float(input('Choose the number of translate: '))
    s = input('Enter the string: ')
    str = ''

    if x == 1:
        for item in s:
            if item in alpha.keys():
                str += alpha.get(item)
        print("Decoding: ", str)
    else:
        inv = {first_low_part_of_decrypt: k for k, first_low_part_of_decrypt in alpha.items()}
        for item in s:
            if item in inv.keys():
                str += inv.get(item)
        print('Encoding: ', str)

ROT13()
