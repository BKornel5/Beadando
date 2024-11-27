class BK_Morse:

    # Morse kód táblázat
    Morse_Dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
        "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
        '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
    }


    def text_to_morse(self, text):
        return ' '.join(BK_Morse.Morse_Dict.get(char.upper(), '') for char in text)


    def morse_to_text(self, morse):
        reverse_dict = {value: key for key, value in BK_Morse.Morse_Dict.items()}
        words = morse.split('  ')
        translated_words = []
        for word in words:
            translated_word = ''.join(reverse_dict.get(code, '') for code in word.split())
            translated_words.append(translated_word)
        return ' '.join(translated_words)


