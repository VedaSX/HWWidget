from src.widget import get_date, mask_account_card

account = input("Введите номер карты или счета: ")
print(mask_account_card(account))

date = input("Введите дату: ")
print(get_date(date))
