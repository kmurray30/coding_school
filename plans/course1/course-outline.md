# Course 1 Outline: Intro to Coding (Python)

## Prerequisites

**Required:** Course 0 (Developer Bearings) - Terminal navigation, VSCode basics, running Python files

**Skills needed:**
- Navigate filesystem using `cd`, `ls`, `pwd`
- Create and edit `.py` files in VSCode
- Run Python files from terminal and VSCode
- Read basic syntax errors

## Course Overview

This course takes students from "I can run a file" to "I can write small programs with control flow and functions." By the end, students will write programs that take input, make decisions, loop over data, organize code into functions, and manage dependencies.

**Total estimated time:** 20-25 hours

---

## Unit 1: Output + Basic Programs

**Core Concepts:**
- Printing output
- Sequentiality (code runs top-to-bottom)
- Variables store results for later use

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_hello** - [Observation] Run a program that prints "Hello World!". See output. Introduces `print()`.
2. **exercise2_syntax** - [Observation] See what happens with missing quotes, parentheses. Introduces syntax errors.
3. **exercise3_variables** - [Guided] Assign values to variables, print them. Introduces variable assignment with `=`.
4. **exercise4_practice** - [Guided] Create your own variables with different values. Practice assignment and printing.
5. **exercise5_input** - [Semi-independent] Use `input()` to get user input and print it back. Introduces interactive programs.
6. **exercise6_input_vars** - [Semi-independent] Store user input in a variable, use it multiple times. Reinforces variables + input.
7. **exercise7_greeting** - [Semi-independent] Ask user for name, print personalized greeting. Combines input, variables, and output.
8. **exercise8_mad_libs** - [Project-scale] Create a Mad Libs program. Ask for multiple inputs (noun, verb, adjective), construct a story, print result. Integrates all unit concepts.

**Quiz Topics:**
- What does `print()` do?
- What is a variable?
- How do you get user input?
- What happens when code runs top-to-bottom?
- What's a syntax error vs runtime error?

**Grading Notes:**
- Test approach: Simple output matching for print exercises; skip auto-grading for interactive `input()` exercises (self-check only)
- Required test coverage: Basic correctness - does it print the expected text?
- Special considerations: Exercises 5-8 use `input()`, so grader skips these or they're self-validated

---

## Unit 2: Primitive Types + Strings

**Core Concepts:**
- Primitive types: `int`, `float`, `str`, `bool`
- Type checking with `type()`
- Type casting (`int()`, `str()`, `float()`)
- String concatenation

**Exercise Count:** 10 exercises

**Exercises:**

1. **exercise1_strings** - [Observation] See strings in quotes, print them. Introduces `str` type.
2. **exercise2_ints** - [Observation] See integers, print them, do basic math. Introduces `int` type.
3. **exercise3_math_ops** - [Guided] Practice addition, subtraction, multiplication, division. Reinforces numeric types.
4. **exercise4_type_function** - [Guided] Use `type()` to check variable types. Introduces type introspection.
5. **exercise5_floats** - [Semi-independent] Work with decimal numbers. Introduces `float` type.
6. **exercise6_casting** - [Semi-independent] Convert between types using `int()`, `str()`, `float()`. Introduces type casting.
7. **exercise7_cast_error** - [Observation] See what happens when casting fails (e.g., `int("hello")`). Introduces `ValueError`.
8. **exercise8_float_to_int** - [Guided] Cast float to int, observe truncation. Reinforces casting behavior.
9. **exercise9_booleans** - [Semi-independent] Work with `True` and `False`. Introduces `bool` type.
10. **exercise10_string_builder** - [Project-scale] Ask user for multiple pieces of info (name, age, city), use casting to convert age to int, build a formatted bio string, print result. Integrates types, casting, and string concatenation.

**Quiz Topics:**
- What are the primitive types in Python?
- What does `type()` return?
- How do you convert a string to an integer?
- What happens if you add a string and an int?
- What's the difference between `int` and `float`?

**Grading Notes:**
- Test approach: Output matching for observation exercises; verify correct types for type-checking exercises
- Required test coverage: Basic correctness - right output, right types
- Special considerations: Test that casting exercises produce correct types, not just correct output

---

## Unit 3: Functions (Using and Creating)

**Core Concepts:**
- Using built-in functions (`len()`, `lower()`, `upper()`)
- Creating custom functions with `def`
- Function parameters and return values
- Nested function calls vs intermediate variables

**Exercise Count:** 9 exercises

**Exercises:**

1. **exercise1_sequentiality** - [Observation] See how code flows step-by-step, results stored and used later. Reinforces execution order.
2. **exercise2_len_function** - [Guided] Use `len()` to get string length. Introduces built-in functions.
3. **exercise3_input_len** - [Semi-independent] Ask user for input, print length of their input. Combines `input()` and `len()`.
4. **exercise4_nested_functions** - [Observation] See nested function calls like `print(len(input()))`. Introduces function composition.
5. **exercise5_lowercase** - [Guided] Use `.lower()` method to convert string to lowercase. Introduces string methods.
6. **exercise6_string_concat** - [Semi-independent] Combine strings using `+` operator. Reinforces concatenation.
7. **exercise7_name_greeting** - [Semi-independent] Take user name, convert to uppercase, greet them. Combines methods and concatenation.
8. **exercise8_define_function** - [Challenge] Create your first function that takes a parameter and returns a value. Introduces `def` and `return`.
9. **exercise9_calculator** - [Project-scale] Define multiple functions (add, subtract, multiply, divide), take user input for two numbers and an operation, call the appropriate function, print result. Integrates function definition, parameters, return values, and user input.

**Quiz Topics:**
- What does `len()` do?
- How do you define a function in Python?
- What's the difference between printing and returning?
- What are function parameters?
- What does `return` do?
- Can you call a function before it's defined?

**Grading Notes:**
- Test approach: Output matching for early exercises; function signature/behavior checking for exercises 8-9
- Required test coverage: Verify functions exist, accept correct parameters, return correct values
- Special considerations: Test that functions actually return values, not just print them

---

## Unit 4: Imports and Libraries

**Core Concepts:**
- What an `import` statement does
- Using imported functions
- Different import styles (`import math` vs `from math import sqrt`)
- Finding and using documentation

**Exercise Count:** 7 exercises

**Exercises:**

1. **exercise1_import_math** - [Observation] Import `math` module, use `math.sqrt()`. Introduces `import`.
2. **exercise2_from_import** - [Guided] Use `from math import pi`, access `pi` directly. Introduces `from ... import`.
3. **exercise3_multiple_imports** - [Guided] Import multiple items from same module. Reinforces import syntax.
4. **exercise4_random** - [Semi-independent] Import `random`, use `random.randint()` to generate random numbers. Introduces new module.
5. **exercise5_datetime** - [Semi-independent] Import `datetime`, get current date/time. Introduces another common module.
6. **exercise6_documentation** - [Challenge] Given a module name, explore its functions using `help()` or online docs. Introduces self-directed learning.
7. **exercise7_dice_roller** - [Project-scale] Create a dice rolling program. Import `random`, define a function that simulates rolling N dice, ask user how many dice and how many sides, print results. Integrates imports, functions, and user input.

**Quiz Topics:**
- What does `import` do?
- What's the difference between `import math` and `from math import sqrt`?
- How do you use a function from an imported module?
- Where can you find documentation for Python modules?
- What's the difference between built-in functions and imported functions?

**Grading Notes:**
- Test approach: Verify correct import statements exist; verify correct module usage
- Required test coverage: Basic correctness - imports work, functions are called correctly
- Special considerations: Random output makes exact matching impossible; verify program runs and produces reasonable output

---

## Unit 5: Branching

**Core Concepts:**
- Boolean expressions (comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- `if` / `elif` / `else` statements
- Nested conditionals

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_comparisons** - [Observation] See comparison operators, predict `True`/`False` results. Introduces boolean expressions.
2. **exercise2_string_comparison** - [Guided] Compare strings with `==` and `!=`. Reinforces comparisons.
3. **exercise3_logical_and** - [Guided] Use `and` to combine conditions. Introduces logical operators.
4. **exercise4_logical_or** - [Guided] Use `or` for "either condition". Reinforces logical operators.
5. **exercise5_logical_not** - [Semi-independent] Use `not` to negate conditions. Introduces negation.
6. **exercise6_basic_if** - [Semi-independent] Write an `if` statement that prints different output based on a condition. Introduces `if`.
7. **exercise7_if_else_elif** - [Challenge] Use `if`, `elif`, and `else` to handle multiple cases. Introduces multi-branch logic.
8. **exercise8_age_validator** - [Project-scale] Ask user for age, validate it's a number, check if they're a child (<13), teen (13-17), adult (18-64), or senior (65+), print appropriate message. Integrates casting, comparisons, and multi-way branching.

**Quiz Topics:**
- What comparison operators exist in Python?
- What's the difference between `=` and `==`?
- What does `and` require to be `True`?
- What does `or` require to be `True`?
- When does an `elif` block run?
- Can you have `elif` without `else`?

**Grading Notes:**
- Test approach: Test multiple input scenarios to verify branching logic
- Required test coverage: Test each branch (if, elif, else) is reachable and produces correct output
- Special considerations: Need to provide programmatic input for interactive exercises

---

## Unit 6: Loops - While

**Core Concepts:**
- `while` loop syntax
- Loop conditions
- Infinite loops (and how to avoid them)
- Loop counters
- `break` and `continue`

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_simple_while** - [Observation] See a while loop count from 1 to 5. Introduces `while`.
2. **exercise2_countdown** - [Guided] Write a countdown loop (5, 4, 3, 2, 1, Liftoff!). Reinforces loop logic.
3. **exercise3_user_controlled** - [Semi-independent] Loop until user types "quit". Introduces loop exit conditions.
4. **exercise4_accumulator** - [Semi-independent] Use a loop to sum numbers from 1 to 10. Introduces accumulator pattern.
5. **exercise5_break** - [Guided] Use `break` to exit a loop early. Introduces `break`.
6. **exercise6_continue** - [Guided] Use `continue` to skip loop iterations. Introduces `continue`.
7. **exercise7_validation_loop** - [Challenge] Keep asking user for input until they provide a valid number. Combines loops, casting, and error handling.
8. **exercise8_guessing_game** - [Project-scale] Create a number guessing game. Generate random number, loop while user hasn't guessed it, give "higher" or "lower" hints, count attempts, congratulate when correct. Integrates while loops, conditionals, random, and user input.

**Quiz Topics:**
- What does a `while` loop do?
- How do you exit a while loop?
- What's an infinite loop?
- What does `break` do?
- What does `continue` do?
- What's an accumulator?

**Grading Notes:**
- Test approach: Provide programmatic input to test loop behavior
- Required test coverage: Verify loops run correct number of times, exit on correct conditions
- Special considerations: Interactive loops need input injection for testing; random elements require careful validation

---

## Unit 7: Loops - For

**Core Concepts:**
- `for` loop syntax
- Iterating over sequences (strings, ranges)
- `range()` function
- Nested loops
- Loop vs while (when to use which)

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_range_basic** - [Observation] See `for i in range(5)`, understand iteration. Introduces `for` and `range()`.
2. **exercise2_range_params** - [Guided] Use `range(start, stop, step)` with different parameters. Reinforces `range()`.
3. **exercise3_iterate_string** - [Semi-independent] Loop over each character in a string. Introduces string iteration.
4. **exercise4_list_iteration** - [Semi-independent] Loop over a list of items. Introduces list iteration.
5. **exercise5_accumulator** - [Challenge] Sum numbers using a for loop instead of while. Reinforces for loops.
6. **exercise6_nested_loops** - [Challenge] Use nested loops to print a multiplication table. Introduces nested iteration.
7. **exercise7_pattern_printing** - [Challenge] Use loops to print patterns (pyramids, diamonds). Reinforces nested loops.
8. **exercise8_fizzbuzz** - [Project-scale] Classic FizzBuzz problem. Loop 1-100, print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, otherwise print the number. Integrates for loops, conditionals, and modulo operator.

**Quiz Topics:**
- What does `range(10)` produce?
- What's the difference between `for` and `while` loops?
- How do you iterate over a string?
- What does `range(1, 10, 2)` produce?
- Can you modify a list while iterating over it?
- When should you use `for` vs `while`?

**Grading Notes:**
- Test approach: Exact output matching for pattern exercises; verify correct iteration behavior
- Required test coverage: Verify correct number of iterations, correct output at each step
- Special considerations: FizzBuzz needs exact output verification for all 100 numbers

---

## Unit 8: Scope

**Core Concepts:**
- Local vs global scope
- Function scope
- Variable shadowing
- Why scope matters (avoiding bugs)

**Exercise Count:** 7 exercises

**Exercises:**

1. **exercise1_local_scope** - [Observation] See a variable defined inside a function, observe it's not accessible outside. Introduces local scope.
2. **exercise2_global_scope** - [Observation] See a global variable used inside a function. Introduces global scope.
3. **exercise3_shadowing** - [Guided] Create a local variable with same name as global, observe shadowing. Introduces variable shadowing.
4. **exercise4_modify_global** - [Guided] Try to modify a global variable from inside a function (fails), then use `global` keyword (succeeds). Introduces `global`.
5. **exercise5_return_not_global** - [Semi-independent] Write function that returns a value instead of modifying globals. Reinforces good practices.
6. **exercise6_nested_scope** - [Challenge] See nested function scope (function within function). Introduces closure concepts.
7. **exercise7_refactor_globals** - [Project-scale] Given code that uses global variables poorly, refactor to use function parameters and return values. Integrates scope understanding and clean code practices.

**Quiz Topics:**
- What's the difference between local and global scope?
- Can you access a local variable outside its function?
- What happens when local and global variables have the same name?
- What does the `global` keyword do?
- Why should you avoid global variables?
- What's variable shadowing?

**Grading Notes:**
- Test approach: Verify functions use correct scope; verify global keyword when needed
- Required test coverage: Test that scoping works as expected; verify refactored code produces same output
- Special considerations: Some exercises are conceptual (observation); focus on understanding over testing

---

## Unit 9: Mutability vs Immutability

**Core Concepts:**
- Immutable types: `int`, `float`, `str`, `tuple`
- Mutable types: `list`, `dict`, `set`
- What it means to mutate vs reassign
- Why mutability matters (unexpected side effects)

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_immutable_strings** - [Observation] Try to modify a string character (fails), then reassign (succeeds). Introduces string immutability.
2. **exercise2_mutable_lists** - [Observation] Modify a list element in place. Introduces list mutability.
3. **exercise3_list_methods** - [Guided] Use `.append()`, `.remove()`, `.pop()` to mutate lists. Reinforces mutability.
4. **exercise4_list_vs_tuple** - [Guided] Compare modifying a list vs tuple (tuple fails). Introduces tuples.
5. **exercise5_reference_behavior** - [Challenge] See two variables pointing to same list, modifying one affects both. Introduces reference vs copy.
6. **exercise6_copying_lists** - [Semi-independent] Use `.copy()` or list slicing to create independent copies. Reinforces copying.
7. **exercise7_dict_mutability** - [Semi-independent] Modify dictionaries in place. Introduces dict mutability.
8. **exercise8_shared_state_bug** - [Project-scale] Debug a program where shared mutable state causes unexpected behavior. Fix it by using copies or immutable types. Integrates understanding of mutability and debugging skills.

**Quiz Topics:**
- What types are immutable in Python?
- What types are mutable?
- What happens when you assign one list to another variable?
- How do you create a copy of a list?
- Why does modifying a list inside a function affect the original?
- What's the danger of mutable default arguments?

**Grading Notes:**
- Test approach: Verify correct mutability behavior; test that copies are independent
- Required test coverage: Test mutations occur (or don't) as expected
- Special considerations: Testing reference behavior requires checking multiple variables; debugging exercise is self-check

---

## Unit 10: Python Environments and Dependencies

**Core Concepts:**
- Virtual environments (`venv`)
- Installing packages with `pip`
- `requirements.txt` for reproducibility
- Exploring third-party libraries

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_create_venv** - [Guided, txt] Create a virtual environment using `python3 -m venv myenv`. Introduces venv.
2. **exercise2_activate_venv** - [Guided, txt] Activate the virtual environment. Reinforces venv workflow.
3. **exercise3_pip_install** - [Guided, txt] Use `pip install requests` to install a package. Introduces pip.
4. **exercise4_import_requests** - [Semi-independent, py] Import and use `requests` to fetch a webpage. Introduces third-party libraries.
5. **exercise5_colorama** - [Semi-independent, py] Install and use `colorama` to print colored terminal output. Reinforces package usage.
6. **exercise6_requirements** - [Guided, txt] Create a `requirements.txt` file listing dependencies. Introduces requirements files.
7. **exercise7_faker_data** - [Semi-independent, py] Install `faker`, generate fake names/addresses/emails. Introduces data generation libraries.
8. **exercise8_mini_project** - [Project-scale, py] Create a program that fetches data from a public API using `requests`, processes it, and displays it with colored output using `colorama`. Include a `requirements.txt`. Integrates virtual environments, dependencies, and third-party library usage.

**Quiz Topics:**
- What's a virtual environment?
- Why use virtual environments?
- How do you install a package with pip?
- What's a `requirements.txt` file?
- How do you recreate an environment from `requirements.txt`?
- Where do pip packages get installed?

**Grading Notes:**
- Test approach: Verify virtual environment exists; verify packages are installed; verify programs run successfully
- Required test coverage: Check venv directory exists, requirements.txt has correct format, programs execute
- Special considerations: Mix of `.txt` and `.py` files; some exercises are terminal commands, not code; API calls require network access (may skip auto-grading)

---

## Final Exam

**Coverage:** All 10 units, cumulative review

**Question Count:** Approximately 40-50 questions

**Focus Areas:**
- Output and variables (Unit 1)
- Types and casting (Unit 2)
- Functions - using and defining (Unit 3)
- Imports and libraries (Unit 4)
- Conditionals and boolean logic (Unit 5)
- While loops (Unit 6)
- For loops (Unit 7)
- Scope and globals (Unit 8)
- Mutability vs immutability (Unit 9)
- Virtual environments and dependencies (Unit 10)
- Integration: combining multiple concepts

**Question Style:**
- Ask questions the HARD way (not "What does X do?" but "How do you accomplish Y?")
- Mix of conceptual understanding and code reading
- Some "write the code" questions
- Some "what will this print" questions
- Some "find the bug" questions

---

## Overall Grading Strategy

**Test Rigor:** Simple to moderate output matching for most exercises. Focus on correctness, not edge cases.

**Performance Requirements:** None. This is an introductory course focused on understanding concepts, not optimization.

**Special Challenges:**
- **User input:** Many exercises use `input()`. Grader either provides programmatic input via stdin injection, or skips auto-grading (self-check only).
- **Interactive programs:** Projects with complex user interaction are self-validated by running and comparing to expected behavior.
- **Random output:** Exercises using `random` module cannot be exactly tested; verify program runs and produces reasonable output.
- **Network requests:** Unit 10 exercises that hit APIs may be skipped in auto-grading due to network dependency.

**Grader Complexity:** Moderate test suite. Each unit has:
- `unit_grader.py` - Tests regular exercises (1-7)
- `project_grader.py` - Tests final project exercise (8+)

**Grader Approach:**
- Use `subprocess.run()` to execute exercise files
- Capture stdout and compare to expected output
- For exercises with input, use `subprocess.run(input="...")` to provide test input
- For exercises that cannot be auto-graded (interactive, random, network), include them in README but skip in grader with a note
- Display clear pass/fail messages with helpful error output

**What Gets Auto-Graded:**
- Units 1-3: Most exercises auto-graded; skip complex interactive programs
- Units 4: Auto-grade import statements and basic module usage
- Units 5-7: Auto-grade with programmatic input injection
- Unit 8: Auto-grade scope behavior
- Unit 9: Auto-grade mutability behavior with assertions
- Unit 10: Mix of terminal command verification (check files exist) and code execution (if no network required)

**What Stays Self-Check:**
- Complex interactive programs with multi-step input/output
- Programs with random output (verify it runs, but can't check exact output)
- Programs requiring network access
- Refactoring/debugging exercises (verify understanding through comparison)
