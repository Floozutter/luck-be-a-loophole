from json import loads, dumps

class Save:
    def __init__(self, text: str) -> None:
        self.data = tuple(map(loads, text.strip().split("\n")))
    def __str__(self) -> str:
        return "\n".join(map(dumps, self.data))
    @property
    def coins(self) -> int:
        return int(self.data[2]["coins"])
    @coins.setter
    def coins(self, value: int) -> None:
        self.data[2]["coins"] = value
