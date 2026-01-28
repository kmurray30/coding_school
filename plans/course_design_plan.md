---
name: Course Design Plan
overview: A comprehensive design document outlining the structure, pedagogy, file formats, and testing strategy for building incremental coding courses with personality.
todos: []
---

# Course Design Blueprint

## Overview

This document defines HOW to build coding courses, regardless of specific curriculum content. It establishes the structure, file formats, grading mechanisms, and pedagogical approach for creating courses that build incrementally from beginner to competent programmer.

## Course Architecture

### Course Structure

Each course contains:

- **N Units** (typically 6-12 units per course)
- **1 Final Exam** (single YAML file with questions, no answers)
- **README.md** (simple outline + how to run graders)

### Unit Structure

Each unit contains:

1. **4-12 Exercises** (incremental progression, last 1-2 are project-scale)
2. **1 Quiz** (single YAML file with questions, no answers)
3. **Grader module** (`graders/unit_grader.py` and `graders/project_grader.py`)

## Course Outline Document

### Purpose

The course outline is a **detailed implementation plan** for an AI agent (or human) to build all course files. It lives in `plans/courseN/course_outline.md` and serves as the blueprint before any actual course files are created.

**Key distinction:**
- **`plans/courseN/curriculum.md`** - High-level topics and goals
- **`plans/courseN/course_outline.md`** - Detailed exercise-by-exercise implementation plan
- **`courseN/README.md`** - Student-facing version (similar to curriculum, but in the actual course directory)

### What to Include

A course outline should specify:

1. **Unit-by-Unit Breakdown**
   - Unit title and core concepts
   - Number of exercises planned
   - High-level description of each exercise
   - Incremental skill progression (observation → guided → semi-independent → challenge)
   - Description of final project-scale exercise(s)

2. **Exercise Specifications**
   - What concept each exercise introduces or reinforces
   - Expected difficulty level (easy/medium/hard)
   - General approach (observation, fill-in-the-blanks, write-from-scratch, etc.)
   - What success looks like (expected output or behavior)

3. **Quiz & Exam Planning**
   - Topics to cover in each unit quiz
   - Rough question count
   - Final exam scope and coverage

4. **Grading Considerations**
   - Test rigor required: simple output matching vs comprehensive edge cases vs performance validation
   - What can be auto-graded (exact output matching, pattern matching, etc.)
   - What requires self-check only (subjective tasks, interactive programs with complex input)
   - Edge cases and stress tests needed (especially for DSA courses)
   - Performance/complexity requirements (e.g., must handle 10^6 elements in O(n log n))
   - Special grading challenges for this course's content
   - Approach for handling user input in graded exercises

5. **Prerequisites & Dependencies**
   - What knowledge students need before starting
   - External dependencies or tools required
   - Setup instructions if needed

### Format

Keep it straightforward. Use markdown with clear sections:

```markdown
# Course N Outline: [Course Title]

## Prerequisites
[What students need to know before starting]

## Unit 0: [Topic Name]

**Core Concepts:** [1-3 key concepts]

**Exercise Count:** [N exercises]

**Exercises:**

1. **exercise1_name** - [Observation] Brief description. Introduces [concept].
2. **exercise2_name** - [Guided] Brief description. Reinforces [concept].
3. **exercise3_name** - [Semi-independent] Brief description. Combines [concepts].
...
N. **exerciseN_final_project** - [Project-scale] Brief description. Integrates all unit concepts.

**Quiz Topics:**
- [Topic 1]
- [Topic 2]
...

**Grading Notes:**
- Test approach: [Output matching / edge case coverage / performance validation]
- Required test coverage: [Basic correctness / comprehensive edge cases / stress tests]
- Special considerations: [User input handling / performance requirements / etc.]

## Unit 1: [Topic Name]
[Same structure as Unit 0]

## Final Exam

**Coverage:** All units, cumulative review

**Question Count:** [Approx. 30-50 questions]

**Focus Areas:**
- [Area 1]
- [Area 2]
...

## Overall Grading Strategy

**Test Rigor:** [Simple output matching / Moderate edge case coverage / Comprehensive DSA-style testing]

**Performance Requirements:** [None / Basic efficiency / Strict complexity requirements (O notation)]

**Special Challenges:** [How to handle user input / testing GUI/interactive programs / etc.]

**Grader Complexity:** [Simple script / Moderate test suite / Substantial test framework]
```

### Implementation Workflow

1. Write `curriculum.md` (high-level topics)
2. Write `course_outline.md` (detailed exercise plan)
3. Implement exercises following the outline
4. Write quizzes and graders
5. Copy curriculum to `courseN/README.md` with grader instructions

The outline is the bridge between "what should we teach" and "here are the actual files."

## Exercise Design Patterns

### Progression Philosophy

Exercises within a unit follow an incremental staircase pattern, referenced from [`example/`](example/):

1. **Observation Exercises** (1-2 exercises)

   - Students read code and predict output
   - No modification required
   - Build mental models
   - Example: [`exercise1_sequentiality.py`](example/unit1-basic_functions/exercise1_sequentiality.py)

2. **Guided Modification** (2-3 exercises)

   - Code skeleton provided
   - Students fill in `...` sections
   - Clear expected output shown
   - Example: [`exercise3_logical_and.py`](example/unit3-boolean_logic/exercise3_logical_and.py)

3. **Semi-Independent Tasks** (3-5 exercises)

   - More open-ended requirements
   - Students write larger code sections
   - Multiple approaches possible
   - Example: [`exercise6_number_guessing.py`](example/unit4-if_statements/exercise6_number_guessing.py)

4. **Challenge Exercises** (1-2 exercises)

   - Minimal scaffolding
   - Combines multiple concepts
   - Prepares for projects

### Exercise File Format

**KEEP IT MINIMAL.** Exercises should be bare-bones code with just enough comments to:
- Introduce a new concept (1-3 lines)
- Tell students what to do
- Show expected output

**Learning happens through iteration**, not through reading walls of text.

Reference style from [`example/`](example/) directory.

**Simple observation exercise:**
```python
# Variables store values. Use = to assign.
monkeys = "bananas"
print(monkeys)

# Expected output: ???
```

**Simple modification exercise:**
```python
# Print "Hello world!"
print("Sample text")

# Expected output: Hello World!
```

**Larger exercise (still minimal):**
```python
# Write a program to ask for the user's name and print a greeting.
# Convert the name to uppercase.
# Then tell them how long their name is.

...

# Expected output:
# Type your name
# (wait for user input)
# Hello <NAME>!
# Your name is <length of name> letters long.
```

**NO metadata like "CONCEPT:", "THE DEAL:", "INSTRUCTIONS:", etc.** Just comments and code.

### Variable Naming for Grading

For exercises where students customize values, grader can parse the file for specific variable names like `your_name`, `your_word`, etc.

### Code Execution Progression

**Early units (Course 1-2, Units 1-4):**

- Pure scripts (top-to-bottom execution)
- All code runs when file is executed
- Direct `print()` statements

**Mid units (Course 1-2, Units 5-8):**

- Introduction of functions
- Mix of script-level code and functions
- Students learn to `def` and call functions

**Later units (Course 2+, Advanced topics):**

- Classes and OOP
- Functions as primary structure
- Scripts mainly for testing/demo

**Guideline:** Use the simplest structure that teaches the concept. Don't force OOP onto "print hello world."

## Project-Scale Exercises

**NO separate project files.** The last 1-2 exercises in each unit are project-scale:
- Larger scope than earlier exercises
- Combine multiple concepts from the unit
- More open-ended
- Same minimal comment style as regular exercises

**Example (final exercise in loops unit):**
```python
# Create an asterisk pyramid.
# Ask user for height, then print a pyramid that tall.

...

# Expected output (if user enters 5):
#     *
#    ***
#   *****
#  *******
# *********
```

Same vibe, same structure, same minimal verbosity. Just bigger in scope.

## Quiz & Exam Design

### Quiz Structure (End of Unit)

**Format:** Single YAML file with questions only (NO answers)

**File:** `quiz.yaml`

**Purpose:** Self-reflection and practice. Students look up answers themselves if unsure.

**Question Style:** Ask questions the HARD way
- ❌ "What does pwd do?"
- ✅ "What command prints your current directory?"

**Example YAML:**
```yaml
quiz_title: "Unit 1 Quiz: Basic I/O"
questions:
  - "What command prints your current directory?"
  - "How do you create a variable in Python?"
  - "What will this code print: x = 5; print(x * 2)"
  - "Write the code to ask user for their name and print it."
```

Simple list. No metadata. No answers. Students figure it out or look it up.

### Final Exam (End of Course)

**Format:** Single YAML file, same as quiz but covering all units

**File:** `final_exam.yaml`

**Coverage:** Cumulative review of all course concepts

**Example YAML:**
```yaml
exam_title: "Course 0 Final Exam"
questions:
  - "What command shows files in current directory?"
  - "How do you run a Python file called test.py?"
  - "What's the difference between relative and absolute paths?"
  # ... 30-50 questions total
```

## Personality & Writing Style

### The Vibe: Primeagen Energy

All course content should channel ThePrimeagen's approach:

- **No BS, direct communication** - Don't waste words
- **Opinionated when it matters** - Explain WHY certain practices matter
- **Funny and raunchy** - Keep it entertaining (within reason)
- **Story-driven teaching** - Use anecdotes and war stories
- **Practical over theoretical** - "Here's what actually happens in production"

### When to Be Opinionated

**Do:**

- Explain why `snake_case` > `camelCase` in Python (it's the convention, don't fight it)
- Warn about mutable default arguments (this WILL bite you)
- Advocate for meaningful variable names (your future self will thank you)
- Share real consequences (I've seen production go down because...)

**Don't:**

- Tabs vs spaces religious wars (who cares, just be consistent)
- Editor preferences (use what makes you productive)
- Personal style quirks without rationale

### Example Personality Injections (Keep Minimal)

**For variable naming:**

```python
# Bad variable names will haunt you. Use clear names.
x = "John"  # What is x? Who knows.
user_name = "John"  # Ah yes, the user's name.
```

**For string concatenation:**

```python
# String concatenation is like assembly. Snap pieces together with +

your_name = "Primeagen"
weird_fact = " has a tiny weiner"
message = your_name + weird_fact
print(message)

# Expected output: Primeagen has a tiny weiner
```

**For loops:**

```python
# While loops ask "are we there yet?" until the answer changes.
# For loops visit each item once. More civilized.
```

### Minimal Anecdotes (Later Units)

**For mutable default arguments:**

```python
# John once debugged for 4 hours before realizing he used a list as a default arg.
# Python creates it ONCE, not per call. Every call shared the same list.
# Use None as default and create the list inside the function. Learn from John!
```

Keep it short. Get to the point. Let students code.

## Grader System

### Purpose

**NOT for grading in the traditional sense.** Graders are for self-validation of understanding.

Students should know if they succeeded by running their code and comparing output. Grader is just confirmation.

### Grader Structure

Each unit has two grader modules in `graders/`:

1. **`unit_grader.py`** - Tests all regular exercises in the unit
2. **`project_grader.py`** - Tests the final project-scale exercise(s)

**Students run:**
```bash
python graders/unit_grader.py
python graders/project_grader.py
```

### Grader Implementation

**Basic approach:**
1. Execute each exercise file
2. Capture stdout
3. Compare to expected output (exact match or pattern)
4. Print pass/fail for each exercise

**Example grader:**
```python
import subprocess
import sys

def test_exercise1():
    result = subprocess.run(['python3', 'exercise1_hello.py'], 
                          capture_output=True, text=True)
    expected = "Hello World!"
    assert expected in result.stdout, f"Expected '{expected}', got '{result.stdout}'"
    print("✓ Exercise 1 passed")

def test_exercise2():
    # ... similar
    
if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        # ... all exercises
        print("\nAll exercises passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
```

### Test Thoroughness

**Graders should verify the solution actually works.** Test coverage scales naturally with problem complexity.

**Simple problems = simple tests:**
- "Print hello world" → Check output is "Hello World!"
- Basic variable assignment → Check expected output appears

**Complex problems = comprehensive tests:**

For data structures, algorithms, and advanced topics, graders must verify:

1. **Correctness** - Multiple test cases with known correct outputs
2. **Edge cases** - Empty inputs, single elements, boundary conditions, maximum sizes
3. **Performance/Complexity** - Solutions meet time/space requirements (e.g., must handle 10^6 elements, algorithm must be O(n log n) not O(n²))
4. **Stress testing** - Large inputs, adversarial cases, random test generation

**For advanced courses:**
- Graders may be substantial codebases with test fixtures, helpers, and data generators
- All tests are visible to students
- Tests should be tough enough that mostly-working solutions fail

**Don't over-test simple exercises.** If the exercise is "assign a variable and print it," don't write 50 test cases. Match test rigor to problem complexity.

## File Naming Conventions

### Exercises

```
exerciseN_description.py
```

- N is 1-indexed
- description is snake_case, 1-3 words
- Examples: `exercise1_hello.py`, `exercise5_string_concat.py`

### Quizzes & Exams

```
quiz.yaml          (unit quiz)
final_exam.yaml    (course final)
```

- YAML format: simple list of questions
- NO answers included

## Directory Structure

**Planning Structure:**
```
plans/
└── courseN/
    ├── curriculum.md           # High-level topics and goals
    └── course_outline.md       # Detailed implementation plan
```

**Course Implementation Structure:**
```
courseN/
├── README.md                    # Student-facing: outline + how to run graders
├── unit1_topic_name/
│   ├── exercise1_intro.py
│   ├── exercise2_building.py
│   ├── ...
│   ├── exerciseN_project_scale.py  # Final 1-2 exercises are project-scale
│   ├── quiz.yaml
│   └── graders/
│       ├── unit_grader.py
│       └── project_grader.py
├── unit2_topic_name/
│   └── ...
├── unitN_topic_name/
│   └── ...
└── final_exam.yaml
```

## Pacing & Difficulty Guidelines

### Exercise Pacing

Reference the progression in [`example/`](example/):

**Unit 0 (Absolute Basics):**

- 6-8 exercises
- Very small increments
- Lots of observation exercises
- Build confidence

**Unit 1-3 (Foundation Building):**

- 8-10 exercises
- Moderate increments
- Mix of observation and modification
- Introduce new concepts carefully

**Unit 4+ (Skill Development):**

- 6-8 exercises
- Larger increments
- More independent work
- Fewer scaffolds

**Later Course Units:**

- 4-6 exercises
- Significant increments
- Challenge-oriented
- Expect student autonomy

### Difficulty Curve

Within each unit, exercises should follow this difficulty progression:

1. **Easy** (20% of exercises) - Direct application, one concept
2. **Medium** (50% of exercises) - Combine 2-3 concepts, some problem-solving
3. **Hard/Project-Scale** (30% of exercises) - Final 1-2 exercises are larger, combine multiple concepts, require planning

## Testing Philosophy

Students should know if they succeeded WITHOUT running the grader.

**How:**
- Clear expected output in every exercise
- Minimal friction - run code, compare output, iterate

**Grader role:**
- Self-validation tool
- Confirmation, not primary feedback

**Student workflow:**
```
1. Read exercise (minimal comments)
2. Write code
3. Run code
4. Compare to expected output
5. Iterate until it matches
6. Move on
7. [End of unit] Run grader for validation
```

## Edge Cases & Special Considerations

### Handling User Input in Grading

For exercises with `input()` calls:

- Provide test input programmatically
- Or skip auto-grading and make it self-check only
- Or provide input test cases in comments

### Managing External Dependencies

- Avoid external dependencies in early courses
- When necessary, provide `requirements.txt`
- Keep dependencies minimal and well-documented

### Accessibility

- Use clear, simple language
- Avoid cultural references that don't translate
- Provide examples for abstract concepts
- Don't assume prior knowledge outside prerequisites

### Iteration & Updates

- Course content will evolve
- Track student pain points
- Update exercises that consistently confuse
- Add exercises if gaps emerge
- Remove exercises if redundant

## Success Metrics

A well-designed unit should have:

- **90%+ passing rate** on first quiz attempt
- **Minimal confusion** questions about instructions
- **Progressive difficulty** that feels fair
- **Student engagement** (they actually find it funny/interesting)
- **Transfer of learning** (students apply concepts in projects)

A well-designed course should have:

- **80%+ completion rate** 
- **Clear skill progression** from Unit 1 to final unit
- **Student confidence** to tackle novel problems
- **Positive feedback** about teaching style

---

## Course README Format

Keep it simple. Bulleted outline + how to run graders.

**Example:**
```markdown
# Course 0: Developer Bearings

Learn terminal, VSCode, and running Python.

## Units

- **Unit 0: Terminal & VSCode** - Navigate filesystem, create files
- **Unit 1: Running Python** - Create and execute Python files

## How to Use

1. Work through exercises in order
2. Run your code and compare to expected output
3. At end of each unit, validate with grader:
   ```
   python graders/unit_grader.py
   python graders/project_grader.py
   ```
4. Take quiz (quiz.yaml) for self-reflection
5. Take final exam (final_exam.yaml) after completing all units

## Prerequisites

None. Start here if you're brand new.
```

## Implementation Checklist

When building a new unit:

- [ ] Define 1-2 core concepts
- [ ] Outline 4-12 exercises (last 1-2 are project-scale)
- [ ] Write minimal exercise files (reference example/)
- [ ] Create quiz.yaml with hard-style questions
- [ ] Build unit_grader.py and project_grader.py
- [ ] Test all exercises run correctly
- [ ] Verify incremental difficulty

When building a new course:

- [ ] Write curriculum.md (high-level topics and goals)
- [ ] Write course_outline.md (detailed exercise-by-exercise plan)
- [ ] Build all units following unit checklist and the outline
- [ ] Create final_exam.yaml
- [ ] Write course README.md (student-facing version of curriculum + grader instructions)
- [ ] Test complete course flow