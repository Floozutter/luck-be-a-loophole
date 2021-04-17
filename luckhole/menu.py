from . import Save

def prompt(
    name: str,
    default: Optional[str] = None,
    valid: Callable[[str], bool] = lambda s: True
) -> str:
    text = f"{name} [{default}]: " if default is not None else f"{name}: "
    while True:
        value = input(text).lower()
        if default is not None and not value:
            return default.lower()
        elif valid(value):
            return value

OPTIONS = {
    "help": "show and describe all options",
    "coins": "edit number of coins",
    "removals": "edit number of removal tokens",
    "rerolls": "edit number of reroll tokens",
    "add_item": "add an item by name",
    "add_symbol": "add a symbol by name",
    "discard": "exit without writing to outsavefile",
    "write": "exit and write to outsavefile",
}
def menu(save: Save) -> bool:
    """handles main menu i/o. returns True to write, and False to discard."""
    is_nat = lambda s: s.isdigit()
    while True:
        option = prompt("\noption", "help", lambda s: s in OPTIONS)
        if option == "help":
            for k, v in OPTIONS.items():
                print(f"{k:<{max(map(len, OPTIONS))}} - {v}")
        elif option == "coins":
            save.coins = int(prompt("coins", str(save.coins), is_nat))
        elif option == "removals":
            save.removals = int(prompt("removal tokens", str(save.removals), is_nat))
        elif option == "rerolls":
            save.rerolls = int(prompt("reroll tokens", str(save.rerolls), is_nat))
        elif option == "add_item":
            name = prompt("item name")
            for _ in range(int(prompt("quantity", "1", is_nat))):
                save.add_item(name)
        elif option == "add_symbol":
            name = prompt("symbol name")
            for _ in range(int(prompt("quantity", "1", is_nat))):
                save.add_symbol(symbol)
        elif option == "discard":
            return False
        elif option == "write":
            return True
        else:
            print("sorry, not implemented yet!")
    raise AssertionError("how did you get here?")
