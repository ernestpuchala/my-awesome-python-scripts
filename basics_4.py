party_1 = ["Mati", "Kasia", "Ola", "Julia", "Kacper"]
party_2 = ["Ada", "Iza", "Kasia", "Ernest", "Julia"]

set_party_1 = set(party_1)
set_party_2 = set(party_2)

# Zadanie 1: Wspólna lista gości bez duplikatów 
wspolne_party = set_party_1.union(set_party_2)
print(f"Wszystkie osoby na połączonej imprezie to: {wspolne_party}")

# Zadanie 2: Znalezienie osób lojalnych tylko Ani (różnica zbiorów)
party_1_UNIQUE = set_party_1.difference(set_party_2) 
print(f"Osoby lojalne tylko Ani to: {party_1_UNIQUE}")