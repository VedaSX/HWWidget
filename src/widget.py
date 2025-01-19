def mask_account_card(string: str) -> list:
    new_string = 0
    for i in range(len(string)):
        if string[i].isdigit():
            new_string = i
            break

    account = []
    account.append(string[:new_string].strip())
    account.append(string[new_string:].strip())

    return account



