from typing import Any, Dict, Generator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Any:
    """Функция принимает на вход список словарей и возвращяет итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if len(transactions) > 0:
        filtered_transaction: Any = filter(
            lambda transaction_list: transaction_list.get("operationAmount").get("currency").get("code") == currency,
            transactions,
        )
        return filtered_transaction
    else:
        return "Пустой Список!"


def transaction_descriptions(transactions: list[dict]) -> Generator[Dict, None, None]:
    """Возвращает описание каждой транзакции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт в заданном диапазоне."""
    for number in range(start, end + 1):
        yield f"{number:016}"
