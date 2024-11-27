# Morse kód fordító (Morse Code Translator)

Hallgató

Név: Bertók Kornél István (LF8QV6)


## Feladat leírása

Ez egy olyan program, amivel szövegeket lehet Morse kódra fordítani, vagy épp Morse kódot szöveggé alakítani.
Az egészet egy könnyen használható ablakos alkalmazásban oldottam meg.


## Modulok és a modulokban használt függvények osztály(ok)


### 1. BK_morse.py 

Osztály: BK_Morse
text_to_morse(self, text): Szöveget Morse kódra alakít.
morse_to_text(self, morse): Morse kódot szöveggé alakít.

### 2. tkinter 

Tk(): Az ablak létrehozása.
Label(): Szöveges címkék a grafikus felületen.
Text(): Szövegmezők, ahol beírható vagy kiolvasható a szöveg.
Button(): Gombok létrehozása és eseménykezelés.

### 3. main.py 

Függvények:
text_to_morse(): Szöveget Morse kódra fordít a GUI-n belül.
morse_to_text(): Morse kódot szöveggé fordít a GUI-n belül.