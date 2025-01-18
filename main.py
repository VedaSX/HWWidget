from src.masks import get_card_mask_number, get_mask_account

card_number = input("Введите номер карты: ")
print(get_card_mask_number(card_number))

account_number = input("Введите номер счета: ")
print(get_mask_account(account_number))
