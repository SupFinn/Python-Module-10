from functools import lru_cache, singledispatch, partial
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError("Unsupported operation")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }


def memoized_fibonacci(n: int) -> int:
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    return fib(n)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(arg):
        return "Cannot cast spell"

    @cast_spell.register
    def _(arg: int):
        return f"Damage spell hits with {arg} damage"

    @cast_spell.register
    def _(arg: str):
        return f"Enchantment spell: {arg}"

    @cast_spell.register
    def _(arg: list):
        return f"Casting Multiple Spells: {', '.join(arg)}"

    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    num_list = [10, 20, 30, 40]
    print(spell_reducer(num_list, "add"))
    print(spell_reducer(num_list, "multiply"))
    print(spell_reducer(num_list, "max"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
