# Course 0: Developer Bearings
## Terminal + VSCode + Git

**Course Goal:** Get students comfortable navigating a development environment and running code before diving into actual programming concepts. By the end, students should feel confident opening a terminal, navigating directories, creating/editing files in VSCode, and running Python scripts.

**Prerequisites:** None. This is the absolute starting point.

**Estimated Duration:** 2-3 weeks for typical student

---

## Course Structure Overview

- **2 Units**
- **15 Total Exercises** (7 in Unit 0, 8 in Unit 1)
- **2 Projects** (1 per unit)
- **6 Quiz Versions** (3 per unit)
- **3 Final Exam Versions**

---

## Unit 0: Terminal/CLI + VSCode Essentials

**Core Concepts:**
1. Terminal navigation and the file system
2. Creating and editing files in VSCode
3. Understanding working directories and file paths

**Learning Outcomes:**
- Navigate the file system using `pwd`, `ls`, `cd`
- Understand relative vs absolute paths
- Create, open, and edit files in VSCode
- Understand the concept of "current directory"
- Read program output in the terminal

### Exercises (7 total)

#### Exercise 1: Where Am I? (pwd and terminal basics)
**Type:** Observation + Execution  
**Difficulty:** Easy  
**Concepts:** Terminal basics, `pwd` command, understanding output

**Instructions:**
- Students open terminal and run `pwd`
- Explanation of what "working directory" means (your current location)
- Analogy: GPS coordinates for your terminal session
- Expected output: Their current path displayed

**File:** `exercise1_where_am_i.py`  
**Grading:** Self-check (students verify they see output)

---

#### Exercise 2: What's in Here? (ls command)
**Type:** Observation + Execution  
**Difficulty:** Easy  
**Concepts:** `ls` command, listing directory contents

**Instructions:**
- Students run `ls` to see what's in their current directory
- Run `ls -la` to see hidden files and details
- Explanation: This is like opening a folder in Finder/Explorer, but in text
- Expected output: List of files/directories

**File:** `exercise2_whats_in_here.py`  
**Grading:** Self-check (students verify they see their files)

---

#### Exercise 3: Moving Around (cd command)
**Type:** Guided Modification  
**Difficulty:** Easy  
**Concepts:** `cd` command, navigation between directories

**Instructions:**
- Create a practice directory structure first
- Students practice: `cd folder_name`, `cd ..`, `cd ~`
- Verify location with `pwd` after each move
- Analogy: cd is like clicking folders, `..` is the back button
- Expected output: Students end up in a specific target directory

**File:** `exercise3_moving_around.py`  
**Grading:** Self-check (students verify final pwd matches target)

---

#### Exercise 4: Paths (relative vs absolute)
**Type:** Guided Modification  
**Difficulty:** Medium  
**Concepts:** Relative paths, absolute paths, `/` vs `~` vs `.` vs `..`

**Instructions:**
- Students navigate using both relative and absolute paths
- Understand `/Users/name/folder` vs `./folder` vs `../folder`
- Practice navigating the same location multiple ways
- Expected output: Reach same directory via different path types

**File:** `exercise4_paths.py`  
**Grading:** Self-check (students document 3 different paths to same location)

---

#### Exercise 5: Create and Open Files in VSCode
**Type:** Guided Modification  
**Difficulty:** Medium  
**Concepts:** VSCode file creation, opening folders, editor basics

**Instructions:**
- Open VSCode from terminal: `code .` (opens current directory)
- Create new file in VSCode
- Save file with specific name
- Verify file exists using `ls` in terminal
- Expected output: File appears in both VSCode and terminal listing

**File:** `exercise5_create_files.py`  
**Grading:** File existence check (grader verifies specific file exists)

---

#### Exercise 6: Edit and Save
**Type:** Guided Modification  
**Difficulty:** Medium  
**Concepts:** Editing text in VSCode, saving, keyboard shortcuts

**Instructions:**
- Open provided text file in VSCode
- Make specific changes to the content
- Save using Cmd+S (Mac) or Ctrl+S (Windows)
- Verify changes persist after closing and reopening
- Expected output: File contains expected modified text

**File:** `exercise6_edit_save.py`  
**Grading:** File content check (grader verifies specific text exists)

---

#### Exercise 7: Your First Workspace
**Type:** Semi-Independent  
**Difficulty:** Hard  
**Concepts:** Directory structure, organizing projects, VSCode workspace

**Instructions:**
- Create a project directory structure from scratch
- Navigate to appropriate locations
- Create multiple files and folders
- Open the entire project in VSCode
- Expected output: Specific directory tree structure exists

**File:** `exercise7_workspace.py`  
**Grading:** Directory structure validation (grader checks folder/file tree)

---

### Unit 0 Projects

#### Project 1: Build Your Dev Environment
**File:** `project1_dev_environment.txt`

**Overview:**
You're going to set up a complete workspace for a hypothetical project. This combines all the terminal and VSCode skills you've learned. Think of this as building the foundation before you build the house.

**Requirements:**
1. Create a directory called `my_first_project` in your home directory
2. Inside it, create three subdirectories: `code`, `notes`, `resources`
3. In the `code` directory, create three empty Python files: `main.py`, `helpers.py`, `tests.py`
4. In the `notes` directory, create a text file called `ideas.txt` with at least 3 lines of text
5. In the `resources` directory, create a file called `links.txt` with at least 2 URLs
6. Open the entire `my_first_project` folder in VSCode
7. Take a screenshot showing: terminal with directory tree AND VSCode with all files visible

**Function to Create:**
None (this is pure terminal/VSCode work)

**Grading Criteria:**
- Correctness: All directories and files exist in correct locations
- Structure: Proper nesting and organization
- Content: Required content in text files exists
- Evidence: Screenshot shows complete setup

**Example Structure:**
```
~/my_first_project/
├── code/
│   ├── main.py
│   ├── helpers.py
│   └── tests.py
├── notes/
│   └── ideas.txt
└── resources/
    └── links.txt
```

**Tips:**
- Use `mkdir -p` to create nested directories in one command
- Use `touch` to create empty files quickly (or create them in VSCode)
- Use `tree` command (if installed) to visualize your directory structure
- Remember: `cd` to navigate, `pwd` to verify location before creating files

---

### Unit 0 Quizzes

**Quiz Coverage:** Terminal commands (pwd, ls, cd), paths (relative/absolute), VSCode basics (create, edit, save files), directory navigation

**Format:** 15 questions total
- 6 questions: Concept understanding ("What does `cd ..` do?")
- 6 questions: Command prediction ("If you're in `/Users/name/projects` and run `cd ../..`, where will you be?")
- 3 questions: Applied problem-solving ("Which command sequence creates a file in a new directory?")

**Passing Threshold:** 90% (14/15 correct)

#### Quiz 1 (Primary)
**File:** `quiz1.json`
- Straightforward questions covering all exercises
- Direct application of concepts learned
- Example: "What command shows your current directory?"

#### Quiz 2 (Optional - if Quiz 1 < 90%)
**File:** `quiz2.json`
- Same concepts, different phrasing and examples
- Equal difficulty to Quiz 1
- Example: "Which command displays your present working directory?"

#### Quiz 3 (Optional - if Quiz 2 < 90%)
**File:** `quiz3.json`
- Same concepts, different scenarios
- Equal difficulty to Quiz 1 and 2
- Example: "How do you check which folder you're currently in?"

---

## Unit 1: Creating and Running Python Files

**Core Concepts:**
1. Creating `.py` files for Python programs
2. Running Python from the terminal
3. Understanding the difference between running in terminal vs editor
4. Reading and interpreting Python output

**Learning Outcomes:**
- Create properly named Python files
- Execute Python scripts from the command line
- Understand the relationship between file location and execution
- Differentiate between terminal execution and VSCode's run button
- Read and understand program output

### Exercises (8 total)

#### Exercise 1: Hello Python (creating your first .py file)
**Type:** Observation + Execution  
**Difficulty:** Easy  
**Concepts:** Creating Python files, `.py` extension, file naming

**Instructions:**
- Create a file called `hello.py` in VSCode
- File contains: `print("Hello, World!")`
- Understand that `.py` tells the computer "this is Python"
- Expected output: File exists and contains the print statement

**File:** `exercise1_hello_python.py`  
**Grading:** File existence and content check

---

#### Exercise 2: Running Python from Terminal
**Type:** Guided Modification  
**Difficulty:** Easy  
**Concepts:** `python` command, `python3` command, running scripts

**Instructions:**
- Navigate to directory containing `hello.py`
- Run: `python3 hello.py`
- Understand what "running a file" means (computer reads and executes code)
- See the output appear in terminal
- Expected output: "Hello, World!" prints in terminal

**File:** `exercise2_running_python.py`  
**Grading:** Self-check (students verify they see output)

---

#### Exercise 3: Terminal vs Editor Run Button
**Type:** Observation  
**Difficulty:** Easy  
**Concepts:** Different ways to execute code, VSCode run button vs terminal

**Instructions:**
- Run the same Python file two ways:
  1. Using VSCode's run button (top right)
  2. Using `python3 filename.py` in terminal
- Observe that output appears in different places
- Understand both execute the same code
- Expected output: Same result from both methods

**File:** `exercise3_terminal_vs_editor.py`  
**Grading:** Self-check (students document both methods work)

---

#### Exercise 4: The Current Directory Matters
**Type:** Guided Modification  
**Difficulty:** Medium  
**Concepts:** Working directory context, path to file when running Python

**Instructions:**
- Create a Python file in a specific folder
- Try to run it from parent directory: `python3 folder/file.py`
- Try to run it from wrong directory: observe error
- Understand Python needs to find the file
- Expected output: Success from correct path, error from incorrect path

**File:** `exercise4_directory_matters.py`  
**Grading:** Self-check (students document success and failure scenarios)

---

#### Exercise 5: Reading Output
**Type:** Guided Modification  
**Difficulty:** Medium  
**Concepts:** `print()` function, console output, reading program results

**Instructions:**
- Create a Python file with multiple `print()` statements
- Run the file
- Observe each print statement produces a line of output
- Understand the connection between code and terminal output
- Expected output: All print statements appear in order

**File:** `exercise5_reading_output.py`  
**Grading:** Output verification (grader checks stdout matches expected)

---

#### Exercise 6: Errors Are Your Friends
**Type:** Observation  
**Difficulty:** Medium  
**Concepts:** Syntax errors, reading error messages, file/line number in errors

**Instructions:**
- Run a Python file with intentional syntax errors
- Read the error message: file name, line number, error type
- Understand errors tell you what's wrong and where
- Fix the errors one by one
- Expected output: Program runs successfully after fixes

**File:** `exercise6_errors_are_friends.py`  
**Grading:** Self-check (students fix all errors and program runs)

---

#### Exercise 7: Multiple Python Files
**Type:** Semi-Independent  
**Difficulty:** Hard  
**Concepts:** Organizing code across files, running specific files

**Instructions:**
- Create 3 different Python files in the same directory
- Each file prints something different
- Practice running each file individually
- Understand that each `.py` file is a separate program
- Expected output: Ability to run each file and get unique output

**File:** `exercise7_multiple_files.py`  
**Grading:** File existence and output verification (grader runs each file)

---

#### Exercise 8: Your First Real Program
**Type:** Semi-Independent  
**Difficulty:** Hard  
**Concepts:** Creating program from scratch, combining all skills

**Instructions:**
- Create a new directory for your program
- Create a Python file that prints your name and a fun fact
- Run it from the terminal
- Modify it to print something different
- Run it again and see the new output
- Expected output: Custom program runs and prints personalized content

**File:** `exercise8_first_real_program.py`  
**Grading:** Custom variable parsing + output verification

---

### Unit 1 Projects

#### Project 1: The Introduction Machine
**File:** `project1_introduction_machine.txt`

**Overview:**
Build a Python program that introduces you to the world. This program will combine everything you've learned about creating files, running Python, and producing output. Think of this as your coding debut—make it memorable.

**Requirements:**
1. Create a directory called `introduction_project`
2. Inside it, create a file called `intro.py`
3. The program must print at least 5 lines of output
4. Line 1: Your name
5. Line 2: Where you're from
6. Line 3: Why you're learning to code
7. Line 4: A weird fact about yourself
8. Line 5: A prediction about your coding future
9. The program must run without errors when executed with `python3 intro.py`
10. Each line should be a separate `print()` statement

**Function to Create:**
None (just top-level print statements)

**Grading Criteria:**
- Correctness: Program runs without errors
- Requirements: All 5+ lines of output present
- Output: Each line contains meaningful content (not just "test")
- File location: Correct directory and file name

**Example Run:**
```
$ python3 intro.py
Kyle Murray
From: Colorado
Why coding: To build things that don't physically fall apart
Weird fact: I've never eaten a banana
Future prediction: I'll write code that makes people laugh and cry
```

**Tips:**
- Use `print("your text here")` for each line
- Remember quotes around your text
- Run your program multiple times to make sure it works
- Have fun with it—personality counts

---

### Unit 1 Quizzes

**Quiz Coverage:** Creating Python files, running Python from terminal, understanding execution, reading output, error messages

**Format:** 18 questions total
- 7 questions: Concept understanding ("What does the `.py` extension indicate?")
- 7 questions: Command/output prediction ("What happens when you run `python3 missing_file.py`?")
- 4 questions: Applied problem-solving ("How do you run a Python file located in a subfolder?")

**Passing Threshold:** 90% (17/18 correct)

#### Quiz 1 (Primary)
**File:** `quiz1.json`
- Covers all Unit 1 exercises
- Direct questions about Python execution
- Example: "What command runs a Python file called `test.py`?"

#### Quiz 2 (Optional - if Quiz 1 < 90%)
**File:** `quiz2.json`
- Same concepts, different file names and scenarios
- Equal difficulty
- Example: "How do you execute a Python script named `program.py`?"

#### Quiz 3 (Optional - if Quiz 2 < 90%)
**File:** `quiz3.json`
- Same concepts, different contexts
- Equal difficulty
- Example: "Which command starts running Python code from `main.py`?"

---

## Course 0 Final Exam

**Coverage:** Comprehensive review of all terminal commands, VSCode operations, Python file creation and execution

**Format:** 30 questions total
- 40% Terminal navigation and commands (Unit 0 focus)
- 40% Python file creation and execution (Unit 1 focus)
- 20% Integrative questions (combining terminal + Python skills)

**Question Distribution:**
- 12 questions: Concept understanding
- 12 questions: Command/output prediction
- 6 questions: Applied problem-solving and troubleshooting

**Passing Threshold:** 90% (27/30 correct)

### Exam 1 (Primary)
**File:** `exam1.json`
- Comprehensive coverage of both units
- Weighted toward practical application
- Example questions:
  - "You're in `/Users/name/projects` and need to run `/Users/name/code/test.py`. What's the command?"
  - "What does `cd ~` do?"
  - "A Python file won't run. The error says 'No such file or directory'. What's the likely problem?"

### Exam 2 (Optional - if Exam 1 < 90%)
**File:** `exam2.json`
- Same concepts, different scenarios
- Equal difficulty to Exam 1
- Different file/folder names and paths
- Different error scenarios

### Exam 3 (Optional - if Exam 2 < 90%)
**File:** `exam3.json`
- Same concepts, completely different problems
- Equal difficulty to Exam 1 and 2
- Fresh examples and scenarios

---

## Grading Breakdown

### Unit 0 Grading
- **Exercises (50%):** 7 exercises, each worth ~7.1%
- **Project (30%):** Project 1 worth 30%
- **Quiz (20%):** Best quiz score out of 3 attempts

**Unit Passing Requirement:** 90% overall with quiz score ≥ 90%

### Unit 1 Grading
- **Exercises (50%):** 8 exercises, each worth 6.25%
- **Project (30%):** Project 1 worth 30%
- **Quiz (20%):** Best quiz score out of 3 attempts

**Unit Passing Requirement:** 90% overall with quiz score ≥ 90%

### Course 0 Final Grade
- **Unit 0:** 40% of final grade
- **Unit 1:** 40% of final grade
- **Final Exam:** 20% of final grade (best of 3 attempts)

**Course Passing Requirement:** 90% overall with final exam score ≥ 90%

---

## Grading Implementation

### Exercise Auto-Grading

**For terminal/VSCode exercises (Unit 0):**
- File existence checks: Does the required file/directory exist?
- File content checks: Does the file contain expected text?
- Directory structure validation: Are folders organized correctly?

**For Python execution exercises (Unit 1):**
- File execution: Can the file run without errors?
- Output capture: Does stdout match expected output?
- Custom variable parsing: Extract student-specific values (name, etc.) and verify they appear in output

### Project Grading

**Semi-automated:**
1. Check file/directory existence
2. Run Python file (if applicable)
3. Capture output
4. Validate against requirements checklist
5. Partial credit for incomplete but correct parts

### Quiz/Exam Grading

**Fully automated:**
- JSON format with questions, answer choices, correct answers
- Multiple choice selection
- Immediate scoring
- Detailed feedback on incorrect answers

---

## Teaching Approach & Personality

Following **Primeagen energy** throughout:

### Key Personality Traits

**Direct and No BS:**
```python
# Terminal navigation is stupidly simple. You're at a location.
# You move to a new location. That's it.
# If you get lost, run `pwd`. Problem solved.
```

**Opinionated When It Matters:**
```python
# Use `python3`, not `python`. Why? Because `python` might point to
# Python 2, which is dead. Like, actually dead. Deprecated in 2020.
# Using `python` is like using Internet Explorer. Don't.
```

**Funny and Memorable:**
```python
# Running `cd ..` is like hitting the back button.
# Running `cd ../../../..` is like rage-clicking the back button
# because you're lost and angry.
```

**Story-Driven:**
```python
# I once spent 30 minutes trying to run a Python file.
# Know what the problem was? I was in the wrong directory.
# The file was literally one folder over. `ls` would have saved me.
# Don't be me. Check where you are before you panic.
```

### When to Be Opinionated

**Do:**
- Explain why `python3` over `python` (version matters)
- Advocate for consistent file naming (snake_case for Python)
- Warn about common mistakes (wrong directory, typos in filenames)
- Share real consequences (lost work from not saving, confusion from bad organization)

**Don't:**
- Tabs vs spaces (too early for this)
- Terminal emulator choice (use what you have)
- VSCode themes (cosmetic preference)

---

## Success Metrics

**Well-designed Course 0 should achieve:**

- **90%+ passing rate** on first quiz attempts (both units)
- **80%+ completion rate** for entire course
- **High confidence** reported by students about terminal and VSCode
- **Low anxiety** about running code (it's just a file, just run it)
- **Smooth transition** into Course 1 (students aren't fighting their tools)

**Red flags to watch for:**

- Students confused about basic navigation
- Repeated errors running Python (indicates directory confusion)
- Fear of terminal (means we're not making it approachable enough)
- Skipping exercises (means difficulty curve is off)

---

## Implementation Checklist

### Unit 0 Implementation
- [ ] Write 7 exercise files with Primeagen personality
- [ ] Create Project 1 instructions file
- [ ] Write 3 quiz versions (15 questions each, unique, equal difficulty)
- [ ] Add expected outputs/success criteria to all exercises
- [ ] Test grader on all exercises
- [ ] Verify terminal commands work on Mac/Linux/Windows
- [ ] Review for clarity and personality consistency

### Unit 1 Implementation
- [ ] Write 8 exercise files with Primeagen personality
- [ ] Create Project 1 instructions file
- [ ] Write 3 quiz versions (18 questions each, unique, equal difficulty)
- [ ] Add expected outputs to all exercises
- [ ] Test grader on all Python executions
- [ ] Verify Python commands work across platforms
- [ ] Review for incremental difficulty

### Course 0 Finalization
- [ ] Write 3 exam versions (30 questions each, comprehensive, equal difficulty)
- [ ] Test complete course flow (Unit 0 → Unit 1 → Exam)
- [ ] Verify learning progression and concept building
- [ ] Create course README with prerequisites and overview
- [ ] Set up grading automation
- [ ] Pilot test with 3-5 beginners and iterate

---

## Appendix: File Structure

```
course0/
├── README.md                           # Course overview and setup
├── unit0_terminal_vscode/
│   ├── exercise1_where_am_i.py
│   ├── exercise2_whats_in_here.py
│   ├── exercise3_moving_around.py
│   ├── exercise4_paths.py
│   ├── exercise5_create_files.py
│   ├── exercise6_edit_save.py
│   ├── exercise7_workspace.py
│   ├── project1_dev_environment.txt
│   ├── quiz1.json
│   ├── quiz2.json
│   └── quiz3.json
├── unit1_python_files/
│   ├── exercise1_hello_python.py
│   ├── exercise2_running_python.py
│   ├── exercise3_terminal_vs_editor.py
│   ├── exercise4_directory_matters.py
│   ├── exercise5_reading_output.py
│   ├── exercise6_errors_are_friends.py
│   ├── exercise7_multiple_files.py
│   ├── exercise8_first_real_program.py
│   ├── project1_introduction_machine.txt
│   ├── quiz1.json
│   ├── quiz2.json
│   └── quiz3.json
├── exam1.json
├── exam2.json
└── exam3.json
```

---

## Next Steps

1. **Implement Unit 0 exercises** following this outline
2. **Implement Unit 1 exercises** following this outline
3. **Create all quiz/exam JSON files** with actual questions
4. **Build grader automation** for exercises and projects
5. **Pilot test** with real beginners
6. **Iterate** based on student feedback and pain points
7. **Document** common student questions for future improvements

**Ready to build.** This course 0 outline provides a complete blueprint for implementation.
