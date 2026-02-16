> *This project has been created as part of the 42 curriculum by rhssayn.*

# 🧙 FuncMage
### *Master the Ancient Arts of Functional Programming*
---

## 📌 Description
**FuncMage** is a Python project focused on mastering **functional programming concepts**:
lambda expressions, higher-order functions, closures, decorators, and functools.

Set in a cyberpunk future of 2142, you'll explore five mystical realms learning powerful functional techniques
to restore balance to the digital realm. Each exercise builds progressive mastery of elegant, reusable code patterns.

---

## 🎯 Project Objectives
- 🔮 Master lambda expressions and anonymous functions
- 📚 Understand higher-order functions and function composition
- 🧠 Explore lexical scoping and closures
- 🏛️ Leverage functools for powerful data manipulation
- ✨ Create decorators and understand class methods
- 💡 Write elegant, functional Python code

---

## 🧪 Exercises Overview

### 🔮 Exercise 0 — Lambda Sanctum
Master anonymous functions using lambda, map, filter, and sorted.
Learn to create quick, powerful spells for data transformation.

**Key Concepts:** lambda, map, filter, sorted, inline functions

---

### 📚 Exercise 1 — Higher Realm
Discover higher-order functions that operate on other functions.
Learn that functions are first-class citizens in Python.

**Key Concepts:** First-class functions, function composition, callable objects

---

### 🧠 Exercise 2 — Memory Depths
Understand lexical scoping and closures that "remember" their environment.
Create persistent magical effects without global variables.

**Key Concepts:** Closures, lexical scoping, nonlocal, state persistence

---

### 🏛️ Exercise 3 — Ancient Library
Explore functools treasures: reduce, partial, lru_cache, singledispatch.
Learn powerful data aggregation and performance optimization.

**Key Concepts:** functools.reduce, partial, lru_cache, singledispatch

---

### ✨ Exercise 4 — Master's Tower
Create decorators and understand @staticmethod.
Prove mastery by transforming function behavior.

**Key Concepts:** Decorators, functools.wraps, @staticmethod, parameterized decorators

---

## ⚙️ Rules & Constraints
- Python **3.10+**
- flake8 compliance required
- **Type hints required** for all functions
- Authorized imports: functools, typing, operator, itertools, standard library
- **Forbidden:** External libraries, file I/O, eval(), global variables
- Focus on functional patterns, not complex algorithms

---

## 📁 Project Structure
```
your-repo/
├── ex0/lambda_spells.py
├── ex1/higher_magic.py
├── ex2/scope_mysteries.py
├── ex3/functools_artifacts.py
└── ex4/decorator_mastery.py
```

---

## 🚀 Execution
```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

---

## 🧪 Exercise Details

### Exercise 0: Lambda Sanctum
Create functions using lambda expressions and anonymous functions.

**Functions to implement:**
- `artifact_sorter(artifacts)` - Sort by power level with lambda
- `power_filter(mages, min_power)` - Filter mages using filter()
- `spell_transformer(spells)` - Transform spell names with map()
- `mage_stats(mages)` - Calculate max/min/avg power with lambdas

**Expected Output:**
```
Testing artifact sorter...
Fire Staff (92 power) comes before Crystal Orb (85 power)
Testing spell transformer...
* fireball * * heal * * shield *
```

---

### Exercise 1: Higher Realm
Create functions that operate on other functions.

**Functions to implement:**
- `spell_combiner(spell1, spell2)` - Combine two spells
- `power_amplifier(base_spell, multiplier)` - Multiply spell results
- `conditional_caster(condition, spell)` - Cast spell conditionally
- `spell_sequence(spells)` - Chain spells in sequence

**Expected Output:**
```
Testing spell combiner...
Combined spell result: Fireball hits Dragon, Heals Dragon
Testing power amplifier...
Original: 10, Amplified: 30
```

---

### Exercise 2: Memory Depths
Use closures to create functions that "remember" state.

**Functions to implement:**
- `mage_counter()` - Return counter function with closure
- `spell_accumulator(initial_power)` - Accumulate power over time
- `enchantment_factory(enchantment_type)` - Create enchantment functions
- `memory_vault()` - Return dict with store/recall closures

**Expected Output:**
```
Testing mage counter...
Call 1: 1
Call 2: 2
Call 3: 3
Testing enchantment factory...
Flaming Sword
Frozen Shield
```

---

### Exercise 3: Ancient Library
Use functools for powerful data manipulation.

**Functions to implement:**
- `spell_reducer(spells, operation)` - Use reduce with operator module
- `partial_enchanter(base_enchantment)` - Create partial applications
- `memoized_fibonacci(n)` - Use lru_cache for performance
- `spell_dispatcher()` - Use singledispatch for type handling

**Expected Output:**
```
Testing spell reducer...
Sum: 100
Product: 240000
Max: 40
Testing memoized fibonacci...
Fib(10): 55
Fib(15): 610
```

---

### Exercise 4: Master's Tower
Create decorators and understand class methods.

**Functions to implement:**
- `spell_timer(func)` - Decorator that times execution
- `power_validator(min_power)` - Parameterized validation decorator
- `retry_spell(max_attempts)` - Decorator that retries on failure
- `MageGuild` class with @staticmethod and decorated methods

**Expected Output:**
```
Testing spell timer...
Casting fireball...
Spell completed in 0.101 seconds
Result: Fireball cast!
Testing MageGuild...
True
False
Successfully cast Lightning with 15 power
Insufficient power for this spell
```

---

## 📦 Authorized Imports

**All exercises:**
- functools (reduce, partial, wraps, lru_cache, singledispatch)
- typing (for type hints)
- operator (for functional operations)
- itertools (for advanced iteration)
- Standard library

---

## 🎓 Learning Outcomes

✅ Create and use lambda expressions effectively  
✅ Understand functions as first-class citizens  
✅ Master higher-order functions and composition  
✅ Use closures for state management  
✅ Apply functools for powerful transformations  
✅ Create decorators that enhance functions  
✅ Use @staticmethod in classes  
✅ Write elegant functional Python code  

---

## 🧠 Functional Programming Philosophy

- **Immutability:** Prefer creating new data over modifying existing
- **Pure Functions:** Functions with no side effects
- **Composition:** Build complex operations from simple functions
- **Higher-Order Functions:** Treat functions as values
- **Closures:** Capture state without globals

---

## 👤 Author

*Created as part of the 42 curriculum — Functional Programming Mastery*

If this project helped you master functional programming, feel free to ⭐ the repository!

**Functional programming makes code more elegant, reusable, and powerful. You've learned to think in terms of functions, composition, and data transformation.** 🧙✨