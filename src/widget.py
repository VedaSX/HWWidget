from src.masks import get_mask_account, get_card_mask_number

def mask_account_card(string: str) -> str:
    """Функция маскирует номер счета и карты"""
    text = ""
    number = ""
    number_count = 0
    for el in string:
        if el.isalpha():
            text += el
        elif el.isdigit():
            number += el
            number_count += 1
    if number_count > 16:
        return f"{text} {get_mask_account(number)}"
    else:
        return f"{text} {get_card_mask_number(number)}"


def get_date(date: str) -> str:
    """Функция форматирует дату"""
    if date.count("-") == 2 and "T" in date:
        date_sep = (date[: date.index("T")]).split("-")

    date_formatted = []

    for date_el in reversed(date_sep):
        date_formatted.append(date_el)

    return ".".join(date_formatted)
