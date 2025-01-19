def mask_account_card(string: str) -> list:
    """Функция выделяет цифры и буквы из строки"""
    new_string = 0
    for i in range(len(string)):
        if string[i].isdigit():
            new_string = i
            break

    account = []
    account.append(string[:new_string].strip())
    account.append(string[new_string:].strip())

    return account


def get_date(date: str) -> str:
    """Функция форматирует дату"""
    if date.count("-") == 2 and "T" in date:
        date_sep = (date[: date.index("T")]).split("-")

    date_formatted = []

    for date_el in reversed(date_sep):
        date_formatted.append(date_el)

    return ".".join(date_formatted)
