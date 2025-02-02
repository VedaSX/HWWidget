import pytest

from src.masks import get_mask_account, get_card_mask_number

@pytest.mark.parametrize(
    "number_card, mask_split_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_mask_card_number(number_card: str, mask_split_card: str) -> None:
    """Функция передает строку сномером карты"""
    assert get_card_mask_number(number_card) == mask_split_card


@pytest.mark.parametrize(
    "account_number, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account(account_number: str, mask_account: str) -> None:
    """Функция передает строку с номером счета"""
    assert get_mask_account(account_number) == mask_account