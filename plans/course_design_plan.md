---
name: Course Design Plan
overview: A comprehensive design document outlining the structure, pedagogy, file formats, and testing strategy for building incremental coding courses with personality.
todos: []
---

# Course Design Blueprint

## Overview

This document defines HOW to build coding courses, regardless of specific curriculum content. It establishes the structure, file formats, and pedagogical approach for creating courses that build incrementally from beginner to competent programmer.

## Course Architecture

### Course Structure

Each course contains:

- **N Units** (typically 6-12 units per course)
- **1 Final Exam** (single YAML file with questions, no answers)
- **1 Cheat Sheet** (single YAML file with quick reference info for later lookup)
- **README.md** (pre-reqs, time estimates, and simple course outline)

### Unit Structure

Each unit contains:

1. **4-12 Exercises** (incremental progression, last 1-2 are project-scale)
2. **1 Quiz** (single YAML file with questions, no answers)

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

4. **Prerequisites & Dependencies**
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

## Unit 1: [Topic Name]
[Same structure as Unit 0]

## Final Exam

**Coverage:** All units, cumulative review

**Question Count:** [Approx. 30-50 questions]

**Focus Areas:**
- [Area 1]
- [Area 2]
...
```

### Implementation Workflow

1. Write `curriculum.md` (high-level topics)
2. Write `course_outline.md` (detailed exercise plan)
3. Implement exercises following the outline
4. Write quizzes
5. Copy curriculum to `courseN/README.md`

The outline is the bridge between "what should we teach" and "here are the actual files."

## Exercise Design Patterns

### Progression Philosophy

**Key Rule: SPOONFEED when introducing NEW concepts, DON'T SPOONFEED when combining concepts.**

Exercises within a unit follow an incremental staircase pattern:

1. **Introducing New Concepts** (1-3 exercises)

   - **Show complete working code** demonstrating the new concept
   - NO blanks (`...`), NO gaps to fill in
   - Students observe and run the code to see it work
   - Minimal comments explaining what the new concept is
   - Expected output at the end
   - Example:
     ```python
     # Strings are text wrapped in quotes
     
     name = "Bobosan"
     message = 'Single quotes work too'
     
     print(name)
     print(message)
     
     # Expected output:
     # Bobosan
     # Single quotes work too
     ```

2. **Practicing the Same Concept** (1-2 exercises)

   - Show working examples of the concept
   - Then ask students to try their own with minimal `...` scaffolding
   - Still focused on ONE concept, not combining yet
   - Example:
     ```python
     # Math operators: + - * /
     
     print(10 + 5)
     print(10 - 5)
     print(10 * 5)
     
     # Now try your own
     print(...)
     print(...)
     
     # Expected output:
     # 15
     # 5
     # 50
     # (your results)
     ```

3. **Combining Concepts** (2-4 exercises)

   - **NO CODE SCAFFOLDING** - just requirements
   - Students must figure out how to combine previously learned concepts
   - Describe WHAT to accomplish, not HOW to code it
   - Multiple approaches possible
   - Example:
     ```python
     # Ask the user for their age.
     # Convert it to an integer.
     # Print whether they can vote (18+).
     
     # Expected output:
     # What is your age?
     # (user types age)
     # You can vote: True (or False)
     ```

4. **Project Exercises** (1-2 exercises at end of unit)

   - Creative goals only, NO code scaffolding
   - Combines ALL concepts from the unit
   - Larger scope than regular exercises
   - Open-ended and fun - let students make it their own
   - Describe the scenario/goal, not step-by-step instructions
   - No prescriptive "do this, then this, then this" - give them freedom

### Exercise File Format

**KEEP IT MINIMAL.** Exercises should be bare-bones code with just enough comments to:
- Introduce a new concept (1-3 lines)
- Tell students what to do
- Show expected output

**Learning happens through iteration**, not through reading walls of text.

**ONE CONCEPT PER EXERCISE.** Each exercise should teach exactly one thing:
- ✅ GOOD: "Practice setting breakpoints"
- ❌ BAD: "Practice setting breakpoints, stepping through code, and finding three different bugs"
- ✅ GOOD: "Add your own print statements to debug"
- ❌ BAD: "Debug this function using prints, then refactor it, then optimize it"

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

**Combining concepts (open-ended):**
```python
# Build a simple name badge generator.
# Ask for the user's name.
# Make the badge show their name in uppercase and tell them something about it.

...

# Expected output (will vary):
# What's your name?
# (user types name)
# 
# ==================
# HELLO, ALEX!
# Your name has 4 letters.
# ==================
```

**NO metadata like "CONCEPT:", "THE DEAL:", "INSTRUCTIONS:", etc.** Just comments and code.

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
- **Creative and open-ended** - give students freedom to make it their own
- **NO CODE SCAFFOLDING** - just describe the goal
- **Instructions describe WHAT to build, not HOW to code it**
  - ✅ "Create a loop that prints each item"
  - ❌ "Create a loop using for i in range(1, 4)"
  - ✅ "Ask the user for their name"
  - ❌ "Use input() to get the user's name"
  - Let students choose their own implementation approach

**CRITICAL:** Project exercises should be **creative goals**, not step-by-step instructions.

- ❌ BAD: Step-by-step instructions ("First create X, then add Y, then print Z")
- ❌ BAD: Providing code structure with `...` for students to fill in
- ❌ BAD: Showing variable names, function calls, or specific implementation details
- ❌ BAD: Requiring exact output format or specific variable names
- ✅ GOOD: Describing a creative goal or scenario
- ✅ GOOD: Letting students choose their own data and implementation
- ✅ GOOD: Showing example output that varies ("yours will be different")
- ✅ GOOD: Making it relatable and fun

**Example 1 (creative and open-ended):**
```python
# Build a friends organizer using a dictionary of lists

# Create a dictionary where:
# - Keys are activity names (like "gaming", "sports", "coding", etc.)
# - Values are lists of friend names who like that activity

# Start with an empty dictionary
# Add at least 3 different activities
# Each activity should have at least 2 friends in it
# Some friends can appear in multiple activities (we all have that one friend who does everything)

# Print the dictionary to see your friend groups
# Print just the friends who like one specific activity
# Print how many total activities you have

...

# Expected output (yours will be different):
# {'gaming': ['Alex', 'Jordan'], 'sports': ['Sam', 'Jordan', 'Casey'], 'coding': ['Alex', 'Taylor']}
# ['Alex', 'Jordan']
# 3
```

**Example 2 (creative scenario):**
```python
# Build a Mad Libs program.
# Ask the user for a noun, verb, and adjective.
# Use their words to create a short story and print it.

...

# Expected output (will vary):
# Give me a noun:
# (user types something)
# Give me a verb:
# (user types something)
# Give me an adjective:
# (user types something)
# 
# Once upon a time, a (adjective) (noun) decided to (verb).
# The end!
```

**Example 3 (too prescriptive - DON'T DO THIS):**
```python
# ❌ BAD - Too step-by-step and prescriptive

# Create a list of your favorite foods
favorite_foods = ...

# Add one more food to the list
...

# Print the first and last items
print(...)
print(...)

# Create a dictionary about yourself
my_info = {
    ...
}

# Add a new key "hobby" with your hobby
...

# This is boring and mechanical. Make it creative instead!
```

No code scaffolding. Just creative goals and freedom to implement.

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

### Cheat Sheet (Course-Level Reference)

**Format:** Single YAML file with quick reference info

**File:** `cheat-sheet.yaml`

**Purpose:** A condensed reference students can return to when they forget specific commands, syntax, or key concepts. This is NOT a tutorial—it's a lookup table.

**Content:** Commands, syntax patterns, and core concepts organized by topic. Keep descriptions brutally short. One-liners preferred.

**Example YAML:**
```yaml
cheat_sheet_title: "Course 0 Cheat Sheet"
sections:
  - title: "Terminal Navigation"
    items:
      - command: "pwd"
        description: "Print current directory"
      - command: "ls"
        description: "List files/folders in current directory"
      - command: "cd folder_name"
        description: "Change to folder_name (relative path)"
      - command: "cd /absolute/path"
        description: "Change to absolute path"
      - command: "cd .."
        description: "Go up one directory"
      - command: "cd ~"
        description: "Go to home directory"
  
  - title: "File Operations"
    items:
      - command: "mkdir folder_name"
        description: "Create new directory"
      - command: "touch file.txt"
        description: "Create empty file"
      - command: "cp source.txt dest.txt"
        description: "Copy file"
  
  - title: "Python Basics"
    items:
      - command: "python3 script.py"
        description: "Run Python file from terminal"
      - command: "print('text')"
        description: "Output text to console"
```

**Rule:** If a student completed your course but forgot something 3 months later, they should be able to find it in the cheat sheet in under 10 seconds.

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

your_name = "Bobosan"
weird_fact = " has a tiny weiner"
message = your_name + weird_fact
print(message)

# Expected output: Bobosan has a tiny weiner
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

## File Naming Conventions

### Exercises

**Universal Rule: ONE FILE PER EXERCISE. Always.**

```
exerciseN_description.ext
```

- N is 1-indexed
- description is snake_case, 1-3 words
- Extension depends on content type:
  - `.py` for Python code exercises
  - `.txt` for non-code exercises (terminal commands, VSCode instructions, etc.)
  - Other extensions as appropriate for the language/content
- Examples: `exercise1_hello.py`, `exercise5_string_concat.py`, `exercise1_pwd.txt`, `exercise3_cd_practice.txt`

**When file type is unclear (not coding), use `.txt` files.**
- IDE/tool instructions (VS Code debugger, terminal commands, etc.)
- Conceptual explanations that don't involve writing code
- Reference material or cheat sheets

Each exercise must be in its own file. Never combine multiple exercises into one markdown file or instruction document.

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
├── README.md                           # Student-facing: prereqs, time estimates, unit overview
├── cheat-sheet.yaml                    # Quick reference for students who forget key concepts
├── unit0_topic_name/                   # Non-code unit example
│   ├── exercise1_concept.txt           # Use .txt for non-code exercises
│   ├── exercise2_practice.txt
│   ├── ...
│   ├── exerciseN_project.txt           # Final 1-2 exercises are project-scale
│   └── quiz.yaml
├── unit1_topic_name/                   # Code unit example
│   ├── exercise1_intro.py              # Use .py for Python code
│   ├── exercise2_building.py
│   ├── ...
│   ├── exerciseN_project_scale.py      # Final 1-2 exercises are project-scale
│   └── quiz.yaml
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

Students should know if they succeeded by running their code and comparing output.

**How:**
- Clear expected output in every exercise
- Minimal friction - run code, compare output, iterate

**Student workflow:**
```
1. Read exercise (minimal comments)
2. Write code
3. Run code
4. Compare to expected output
5. Iterate until it matches
6. Move on
```

## Edge Cases & Special Considerations

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

Keep it simple. Pre-reqs + time estimates + brief unit summary + link to detailed course outline in plans.

**Example:**
```markdown
# Course 0: Developer Bearings

Learn terminal, VSCode, and running Python.

**For detailed course outline and exercise descriptions, see:** [plans/course0/course-outline.md](../plans/course0/course-outline.md)


## Prerequisites

None. Start here if you're brand new.

## Course Units

### Unit 0: Terminal/CLI Fundamentals (10 min)
8 exercises teaching terminal navigation: pwd, ls, cd, mkdir, touch, cp.

### Unit 1: VSCode Essentials (15 min)
7 exercises teaching VSCode workflow: opening folders, creating files, using the integrated terminal.

### Unit 2: Running Python (20 min)
8 Python exercises teaching how to create .py files, run them, and read errors.

### Final Exam (10 min)

**Estimated Total Time:** 55 min

## How to Use

1. Work through exercises in order
2. Run your code and compare to expected output
3. Take quiz (quiz.yaml) for self-reflection after each unit
4. Take final exam (final_exam.yaml) after completing all units
```

**Keep the README concise.** Detailed exercise descriptions live in `plans/courseN/course-outline.md`.

## Implementation Checklist

When building a new unit:

- [ ] Define 1-2 core concepts
- [ ] Outline 4-12 exercises (last 1-2 are project-scale)
- [ ] Write minimal exercise files (reference example/)
- [ ] Create quiz.yaml with hard-style questions
- [ ] Test all exercises run correctly
- [ ] Verify incremental difficulty

When building a new course:

- [ ] Write curriculum.md (high-level topics and goals)
- [ ] Write course_outline.md (detailed exercise-by-exercise plan)
- [ ] Build all units following unit checklist and the outline
- [ ] Create final_exam.yaml
- [ ] Create cheat-sheet.yaml (quick reference for later lookup)
- [ ] Write course README.md (student-facing version of curriculum + time estimates)
- [ ] Test complete course flow