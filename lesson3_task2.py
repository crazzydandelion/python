from smartphone import Smartphone

catalog = [Smartphone("Kenshi", "Armor 32s", "+79749874566"),
           Smartphone("IPhone", "14", "+79856541235"),
           Smartphone("POCO", "C71", "+79658451245"),
           Smartphone("Xiaomi", "Redmi A5", "+79852146358"),
           Smartphone("realme", "NOTE 60x", "+72358896541")]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model} - {smartphone.number}")