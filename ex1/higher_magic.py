
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)

    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
        return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return (lambda *args, **kwargs: spell(*args, **kwargs)
            if condition(*args, **kwargs)
            else "Spell fizzled")


def spell_sequence(spells: list[callable]) -> callable:
    return (lambda *args, **kwargs: 
            [spell(*args, **kwargs) for spell in spells])


def main() -> None:
    print("\nTesting spell combiner...")
    def fireball(target):
         return f"Fireball hits {target}"

    def heal(target):
         return f"Heals {target}"
    combined_spell = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined_spell('Dragon')}")

    print("\nTesting power amplifier...")

    def damage():
         return 10

    aplified_power = power_amplifier(damage, 3)
    print(f"Original: {damage()}, Amplified: {aplified_power()}")


if __name__ == "__main__":
     main()
