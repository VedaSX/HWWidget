from src.masks import get_card_mask_number, get_mask_account


def mask_account_card(string: str) -> str:
    """Функция маскирует номер счета и карты"""
    new_string = string.split(" ")
    number = new_string[-1]
    if len(number) == 20:
        new_string_mask = get_mask_account(number)
        return f"{" ".join(new_string[:-1])} {new_string_mask}"
    elif len(number) == 16:
        new_string_mask = get_card_mask_number(number)
        return f"{" ".join(new_string[:-1])} {new_string_mask}"
    else:
        return f"{"Введите корректный номер счета или карты!"}"


def get_date(date: str) -> str:
    """Функция форматирует дату"""
    if date.count("-") == 2 and "T" in date:
        date_sep = (date[: date.index("T")]).split("-")
    else:
        return f"{"Неверный формат даты"}"
    date_formatted = []

    for date_el in reversed(date_sep):
        date_formatted.append(date_el)

    return ".".join(date_formatted)
