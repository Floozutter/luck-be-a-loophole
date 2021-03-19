from json import loads, dumps

class Save:
    def __init__(self, text: str) -> None:
        self.data = tuple(map(loads, text.strip().split("\n")))
    def __str__(self) -> str:
        return "\n".join(map(dumps, self.data))
