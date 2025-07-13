def check_input_type(user_input):
    try:
        # Próbujemy zamienić przecinek na kropkę, bo Python tak lubi
        normalized_input = user_input.replace(',', '.')
        
        # Próbujemy przekonwertować na float
        float(normalized_input)
        return normalized_input # Udało się, slay!
    except ValueError:
        # Jeśli ValueError się pojawi, to znaczy, że to nie była liczba
        return print("co to kurde") # Womp womp, to tekst

def wypad():
    print("Jaki jest stan twojego konta? (podaj kwotę)")
    stan_konta = float(check_input_type(input()))
    print("Jaki jest twój poziom energii od 1 do 10?")
    poziom_energii = int(float(check_input_type(input())))
    print(poziom_energii)
    if stan_konta > 50 and poziom_energii > 6:
        print("Yasss, idziesz slayować na mieście!")
    elif stan_konta > 50 and poziom_energii <= 6:
        print("Masz hajs, ale jesteś wrakiem. Netflix and chill, queen")
    else:
        print("Womp womp. Siedzisz w domu. Może chociaż posprzątaj.")
    return

wypad()


