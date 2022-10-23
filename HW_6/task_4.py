"""
Створіть функцію <morse_code>, яка приймає на вхід рядок у
вигляді коду Морзе та виводить декодоване значення
(латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive
    - для простоти реалізації - цифри, знаки пунктуацїї,
    дужки, лапки тощо використовуватися не будуть.
    Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
"""


class MorseCodeException(Exception):
    pass


def morse_code(user_line):
    morse_code_dict = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        'SOS': '...---...'
    }

    characters = '.- '

    if all(char in characters for char in user_line):

        user_line += ' '
        code_line = user_line.replace("   ", "  ")
        decoder = ''
        text = ''
        i = 1

        for letter in code_line:
            if (letter != ' '):
                i = 0
                text += letter
            else:
                i += 1
                if i == 2:
                    decoder += ' '
                else:
                    decoder += list(morse_code_dict.keys())[
                        list(morse_code_dict.values()).index(text)
                        ]
                    text = ''

    else:
        raise MorseCodeException('This is not morse code.')

    print(decoder)

    return decoder


user_line = input('Enter morse code:')
morse_code(user_line)
