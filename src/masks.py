def get_card_mask_number(number_card: str) -> str:
    """Выводим скрытый номер карты"""
    if len(number_card) == 16:
        mask_card = number_card[:6] + (len(number_card[6:-4]) * "*") + number_card[-4:]
        mask_split_card = " ".join(mask_card[i * 4 : (i + 1) * 4] for i in range(4))
        return mask_split_card
    else:
        return f"{"Введите 16-ти значный номер карты."}"


def get_mask_account(account_number: str) -> str:
    """Выводим скрытый номер аккаунта"""
    if len(account_number) == 20:
        mask_account = (len(account_number[0:2]) * "*") + account_number[-4:]
        return mask_account
    else:
        return f"{"Введите 20-ти значный номер счета."}"
