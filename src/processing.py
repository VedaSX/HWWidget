from datetime import datetime
from typing import Any, Dict, List

def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтруем словарь по значению ключа state"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(date: List[Dict[str, Any]], revers_order: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список по дате в порядке убывания"""
    return sorted(date, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=revers_order)
