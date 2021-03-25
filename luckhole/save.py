from json import loads, dumps
from functools import partial

save_dumps = partial(dumps, separators = (",", ":"))

class Save:
    def __init__(self, text: str) -> None:
        self.data = tuple(map(loads, text.strip().split("\n")))
    def __str__(self) -> str:
        return "\n".join(map(save_dumps, self.data))
    @property
    def coins(self) -> int:
        return int(self.data[2]["coins"])
    @coins.setter
    def coins(self, value: int) -> None:
        self.data[2]["coins"] = value
    @property
    def removals(self) -> int:
        return int(self.data[9]["removal_tokens"])
    @removals.setter
    def removals(self, value: int) -> None:
        self.data[9]["removal_tokens"] = value
    @property
    def rerolls(self) -> int:
        return int(self.data[9]["reroll_tokens"])
    @rerolls.setter
    def rerolls(self, value: int) -> None:
        self.data[9]["reroll_tokens"] = value
    def add_item(self, item: str) -> None:
        try:
            idx = self.data[8]["item_types"].index(item)
        except ValueError:
            self.data[8]["item_types"].append(item)
            self.data[8]["item_count_data"].append(1)
            self.data[8]["saved_item_data"].append(0)
        else:
            self.data[8]["item_count_data"][idx] = self.data[8]["item_count_data"][idx] + 1
    def add_symbol(self, symbol: str) -> None:
        self.data[3]["icon_types_to_be_added"].append(symbol)
