from address import Address
from mailing import Mailing
to_address = Address("488888", "Sochi", "Stalevarov str.", "45", "653")
from_address = Address("999777", "Moscow", "Gorky Park", "4", "3")

mailing = Mailing(to_address, from_address, 2000, "AB123456789RU")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")