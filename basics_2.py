powiedzonka = ["Vibin'", "Chasing sunsets", "Felt cute, might delete later", "Living my best life", "Just vibing", "Slaying all"]
def usuwanie():
    print("oto powiedzonka na dziś:")
    for item in powiedzonka:
        print(item)
    print("Który opis jest najbardziej cringe? (podaj numer od 1 do 6)")   
    cringe = int(input())
    if cringe > 0 and cringe < 7: 
        usunięty_element = powiedzonka.pop(cringe - 1)
        print(f"okej, wyjebalismy {usunięty_element} powiedzonko")
    for item in powiedzonka:
        print(item)
usuwanie()
