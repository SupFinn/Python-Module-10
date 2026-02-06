
def mage_counter() -> callable:
    counter: int = 0
    def calls_counter():
        nonlocal counter
        counter += 1
        return counter
    return calls_counter


def spell_accumulator(initial_power: int) -> callable:
    total_power: int = initial_power
    def power_accumulator(power_to_add):
        nonlocal total_power
        total_power += power_to_add
        return total_power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type.capitalize()} {item_name.capitalize()}"
    return enchanter


def memory_vault() -> dict[str, callable]:
    memory = {}
    def store(key, value):
        nonlocal memory
        memory[key] = value

    def recall(key):
        nonlocal memory
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    enchant_sword = enchantment_factory("Flaming")
    print(enchant_sword("sword"))
    enchant_sheild = enchantment_factory("Frozen")
    print(enchant_sheild("sheild"))


if __name__ == "__main__":
    main()
