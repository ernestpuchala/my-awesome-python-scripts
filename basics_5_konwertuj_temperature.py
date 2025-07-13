def konwertuj_temperature():
    print("podaj temperaturę w stopniach Celsjusza:")
    temperatura_celsjusz = float(input())
    print("podaj jednostkę docelową Fahrenheit (F) lub Kelvin (K)")
    jednostka_docelowa = input().strip().upper()
    if jednostka_docelowa == 'F':
        temperatura_fahrenheit = temperatura_celsjusz * 1.8 + 32
        print(f"temperatura w Fahrenheit to: {temperatura_fahrenheit:.2f} F")
    elif jednostka_docelowa == 'K':
        temperatura_kelvin = temperatura_celsjusz + 273.15
        print(f"temperatura w Kelvin to: {temperatura_kelvin:.2f} K")
    else:
        print("Co to niby jest? Podaj F lub K!")



while True:
    konwertuj_temperature()
    while True:
        kontynuuj = input("Czy chcesz kontynuować? (t/n): ").strip().lower()
        if kontynuuj == 'n':
            print("nie to nie, nara!")
            break 
        elif kontynuuj == 't':
            print("Ok, lecimy dalej! 💅")
            break
        else:
            print("Nie rozumiem, gyat! Napisz 't' lub 'n', proszę.")
    if kontynuuj == 'n':
        break 