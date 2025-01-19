from src.widget import mask_account_card, get_date

account = input("Введите номер карты или счета: ")
print(mask_account_card(account))

date = input("Введите дату: ")
print(get_date(date))
