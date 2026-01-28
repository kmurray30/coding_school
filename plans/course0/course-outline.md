# Course 0 Outline: Developer Bearings

## Course Overview

**Title:** Developer Bearings: Terminal + VSCode + Git

**Goal:** Students will feel comfortable navigating a codebase and running code before learning programming concepts. This course focuses on the practical skills needed to operate in a development environment.

## Prerequisites

None. This is the absolute starting point. Students need:
- A computer with terminal access
- VSCode installed (installation guide will be provided)
- Python 3.x installed (installation guide will be provided)

## Unit 0: Terminal/CLI Fundamentals

**Core Concepts:**
- Terminal navigation and the concept of "current directory"
- File system paths (relative vs absolute)
- Basic file/directory manipulation

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_pwd** - [Observation] Run `pwd` and observe output. Introduces concept of "where am I?" Expected: Students see their current path.

2. **exercise2_ls** - [Observation] Run `ls` and observe what files/folders appear. Introduces listing directory contents. Expected: Students see current directory contents.

3. **exercise3_cd_practice** - [Guided] Navigate to home directory, Desktop, then back. Use `pwd` to verify location. Reinforces navigation. Expected: Students successfully change directories.

4. **exercise4_absolute_vs_relative** - [Guided] Practice using both `/Users/...` (absolute) and `../folder` (relative) paths. Introduces path concepts. Expected: Students understand difference between path types.

5. **exercise5_mkdir** - [Semi-independent] Create a new directory called `my_first_project`. Navigate into it. Verify with `pwd`. Expected: New directory created and navigated to.

6. **exercise6_touch** - [Semi-independent] Create three empty files using `touch`: `file1.txt`, `file2.txt`, `file3.txt`. List them with `ls`. Expected: Three files created and visible.

7. **exercise7_cp** - [Semi-independent] Copy `file1.txt` to `file1_backup.txt`. Verify with `ls`. Expected: File successfully copied.

8. **exercise8_terminal_project** - [Project-scale] Create a directory structure for a coding project: `my_app/` with subdirectories `src/`, `tests/`, `docs/`. Create a `README.txt` in the root. Navigate through structure using both relative and absolute paths. Expected: Complete directory structure with proper organization.

**Quiz Topics:**
- What command shows your current directory?
- How do you list files in a directory?
- What's the difference between `cd folder` and `cd /folder`?
- How do you create a new directory?
- What does `touch` do?
- How do you copy a file?
- What is a relative path? What is an absolute path?
- Why does "current directory" matter when running commands?

**Grading Notes:**
- **Test approach:** Self-check only (interactive terminal commands)
- **Required test coverage:** Skip grading for exercises. For the project, have the grader validate the expected folder and file structure.
- **Special considerations:** None

## Unit 1: VSCode Essentials

**Core Concepts:**
- Using VSCode as a code editor (not just a text editor)
- The relationship between VSCode's file explorer and the terminal
- Running code from the integrated terminal

**Exercise Count:** 7 exercises

**Exercises:**

1. **exercise1_open_folder** - [Observation] Open VSCode. Use "Open Folder" to open a project directory. Observe file explorer on left. Introduces VSCode workspace concept. Expected: Students see folder structure in VSCode.

2. **exercise2_create_file_vscode** - [Guided] Create a new file called `hello.txt` using VSCode (not terminal). Type some text. Save it. Introduces file creation in VSCode. Expected: File created and saved.

3. **exercise3_vscode_terminal** - [Observation] Open VSCode's integrated terminal (View → Terminal or Ctrl+`). Run `pwd` and `ls`. Observe that terminal starts in the opened folder. Expected: Students understand VSCode terminal = regular terminal.

4. **exercise4_edit_and_save** - [Guided] Open an existing file in VSCode. Make changes. Notice the dot on the file tab (unsaved). Save with Cmd+S (Mac) or Ctrl+S (Windows/Linux). Expected: Students understand save workflow.

5. **exercise5_file_explorer_vs_terminal** - [Semi-independent] Create a file using VSCode's file explorer. Create another file using `touch` in VSCode's terminal. List files with `ls`. Observe both files exist. Expected: Students see VSCode and terminal work together.

6. **exercise6_navigate_in_vscode** - [Semi-independent] Open a folder with subdirectories. Use VSCode file explorer to navigate. Use terminal to navigate with `cd`. Open files from both places. Expected: Comfortable navigating both ways.

7. **exercise7_vscode_workflow_project** - [Project-scale] Create a small project structure entirely in VSCode. Make a folder `simple_website/` with files `index.html`, `style.css`, `script.js`. Open each file, add one comment line to each. Practice switching between files using Cmd+P (Mac) or Ctrl+P (quick file switcher). Use both file explorer and quick switcher. Expected: Comfortable VSCode workflow for managing multiple files.

**Quiz Topics:**
- How do you open a folder in VSCode?
- What does the dot on a file tab mean?
- How do you open VSCode's integrated terminal?
- What is the keyboard shortcut to save a file?
- What's the difference between creating a file in VSCode vs terminal?
- Where does VSCode's terminal start (what directory)?
- How do you switch between open files quickly?
- Why use VSCode instead of Notepad/TextEdit?

**Grading Notes:**
- **Test approach:** Self-check only (GUI interactions)
- **Required test coverage:** Skip grading for exercises. For the project, have the grader validate the expected folder and file structure.
- **Special considerations:** None

## Unit 2: Creating and Running Python Files

**Core Concepts:**
- Creating `.py` files
- Running Python from the terminal vs VSCode's run button
- Understanding program output (setting up for "print" concept later)

**Exercise Count:** 8 exercises

**Exercises:**

1. **exercise1_first_py_file** - [Observation] Create a file called `first.py`. Write one line: `print("Hello")`. Save it. Observe the `.py` extension and syntax highlighting. Expected: Students see Python file with colored syntax.

2. **exercise2_run_from_terminal** - [Guided] Run `python3 first.py` from terminal. Observe output appears in terminal. Introduces running Python from CLI. Expected: See "Hello" printed in terminal.

3. **exercise3_vscode_run_button** - [Guided] Click the run button (▶️) in VSCode's top-right while `first.py` is open. Observe output in terminal panel. Introduces VSCode's run feature. Expected: Same output, but initiated from VSCode.

4. **exercise4_modify_and_rerun** - [Semi-independent] Change `first.py` to print a different message. Save. Run again from terminal. Observe new output. Reinforces edit-save-run loop. Expected: New message appears.

5. **exercise5_multiple_prints** - [Semi-independent] Create `messages.py` with three `print()` statements (different messages). Run it. Observe all three messages appear in order. Expected: Three lines of output in sequence.

6. **exercise6_current_directory_matters** - [Guided] Navigate to parent directory in terminal. Try to run `python3 exercise6.py`. Observe error. Navigate back to correct directory. Run successfully. Introduces why "current directory" matters. Expected: Students understand file must be in current directory or use path.

7. **exercise7_syntax_error** - [Observation] Create a file with intentional Python syntax error (e.g., `prin("hello")` instead of `print`). Run it. Observe error message. Fix it. Run again. Introduces error messages and debugging loop. Expected: Students see error, understand how to read it, fix the code.

8. **exercise8_python_workflow_project** - [Project-scale] Create a multi-file Python project: `greeting_app/` with three files: `greeting1.py`, `greeting2.py`, `greeting3.py`. Each file should print a different greeting message. Practice running each file from terminal. Create a `run_all.sh` script (or just document the commands) to run all three in sequence. Expected: Comfortable creating, editing, and running multiple Python files. Understand workflow for a multi-file project.

**Quiz Topics:**
- What file extension do Python files use?
- How do you run a Python file from the terminal?
- What does the VSCode run button (▶️) do?
- Why do you need to save before running?
- What happens if you try to run a file from the wrong directory?
- What is a syntax error?
- How do you read a Python error message?
- What does `print()` do? (High-level: makes output appear)
- Can you run Python code without VSCode? How?

**Grading Notes:**
- **Test approach:** Simple output matching for Python files
- **Required test coverage:** Verify each `.py` file produces expected output when run
- **Special considerations:** 
  - Can auto-grade by running each Python file and checking stdout
  - Error exercise (exercise7) should be self-check (students verify they saw error, then fixed it)
  - Multi-file project (exercise8) can be partially auto-graded (verify each file runs and produces output)
  - Grader should verify files exist and produce expected output

## Final Exam

**Coverage:** All three units - cumulative review of terminal, VSCode, and Python file basics

**Question Count:** Approximately 25-30 questions

**Format:** YAML file with questions only (no answers)

**Focus Areas:**
- Terminal navigation and commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`)
- Path concepts (relative vs absolute)
- VSCode operations (opening folders, creating files, running terminal, keyboard shortcuts)
- Python file workflow (creating `.py` files, running from terminal, running from VSCode)
- Understanding output and errors
- The relationship between file system, terminal, and VSCode
- Debugging basics (reading error messages)

**Sample Questions:**
- What command shows your current directory?
- How do you navigate to your home directory?
- What's the difference between a relative and absolute path?
- How do you create a new directory called `projects`?
- What does `touch hello.txt` do?
- How do you open a folder in VSCode?
- Where does VSCode's integrated terminal start?
- What keyboard shortcut saves a file?
- What file extension do Python files use?
- Write the command to run a Python file called `test.py`
- What does `print()` do in Python?
- If you see an error "No such file or directory" when running a Python file, what's the most likely cause?
- How do you know if a file has unsaved changes in VSCode?
- Can you run Python code without VSCode? If so, how?
- Why is "current directory" important when running commands?

## Overall Grading Strategy

**Test Rigor:** Self-check for terminal/VSCode operations; simple output matching for Python exercises

**Performance Requirements:** None. This course is about comfort and familiarity, not speed or optimization.

**Special Challenges:**
- Most of this course involves interactive tools (terminal, VSCode) that cannot be auto-graded
- Students verify success by comparing their results to provided examples
- Python exercises (Unit 2) can be partially auto-graded using simple output matching
- Emphasis on "did you successfully perform the action?" rather than "did you get the exact right answer?"

**Grader Complexity:**
- **Unit 0 (Terminal):** No auto-grader for exercises. Project grader validates expected folder and file structure.
- **Unit 1 (VSCode):** No auto-grader for exercises. Project grader validates expected folder and file structure.
- **Unit 2 (Python files):** Simple grader script. Run each `.py` file, capture output, verify expected text appears.

**Grader Implementation for Unit 2:**

```python
# graders/unit2_grader.py - Example structure
import subprocess
import os

def run_python_file(filename):
    """Run a Python file and capture output."""
    result = subprocess.run(['python3', filename], 
                          capture_output=True, text=True, timeout=5)
    return result.stdout, result.stderr, result.returncode

def test_exercise(num, filename, expected_in_output):
    """Test a single exercise."""
    if not os.path.exists(filename):
        print(f"✗ Exercise {num}: File '{filename}' not found")
        return False
    
    stdout, stderr, returncode = run_python_file(filename)
    
    if returncode != 0 and num != 7:  # Exercise 7 intentionally has error
        print(f"✗ Exercise {num}: File had errors:\n{stderr}")
        return False
    
    if expected_in_output and expected_in_output not in stdout:
        print(f"✗ Exercise {num}: Expected '{expected_in_output}' in output, got:\n{stdout}")
        return False
    
    print(f"✓ Exercise {num} passed")
    return True

# Tests for each exercise...
```

**Philosophy:**
- Students should already know they succeeded by running their code
- Grader is just confirmation
- For non-gradable items (terminal, VSCode), students follow verification steps
- Keep graders simple - match test rigor to problem complexity

## Teaching Approach

**Personality:** Primeagen energy - direct, practical, occasionally funny

**Key Messages:**
- "You can't break anything. Experiment."
- "The terminal is just a way to talk to your computer. Don't be scared of it."
- "VSCode is a fancy text editor that knows about code. That's it."
- "Running Python is just: `python3 filename.py`. That's literally all there is to it."
- "Errors are feedback, not failure. Read them."

**Minimal Comments Philosophy:**
- Don't over-explain
- Let students discover by doing
- Just enough context to know what to try
- Expected output so they know if they succeeded

**Progression:**
- Start with extreme hand-holding (Unit 0)
- Gradually reduce scaffolding (Unit 1)
- By Unit 2, students are more independent but still guided
- Build confidence through small wins

## Implementation Notes

**Unit 0 Implementation:**
- Cannot create traditional exercise files (these are terminal commands)
- Create documentation/instruction files instead
- Consider creating a `terminal_exercises.md` with step-by-step instructions
- Or create empty "exercise" files that contain instructions in comments
- Verification is manual (student checks their terminal output)

**Unit 1 Implementation:**
- Similar to Unit 0 - mostly GUI interactions
- Create instruction documents with screenshots
- Provide verification checklists
- Students confirm they can perform each action

**Unit 2 Implementation:**
- Traditional Python exercise files
- Can use standard exercise file format
- Grader can actually run and test these
- First unit where auto-grading is possible

**Directory Structure for Course 0:**
```
course0/
├── README.md
├── unit0_terminal/
│   ├── terminal_exercises.md          # Instructions for terminal exercises
│   ├── verification_checklist.md      # How to verify you did it right
│   └── quiz.yaml
├── unit1_vscode/
│   ├── vscode_exercises.md            # Instructions with screenshots
│   ├── verification_checklist.md
│   └── quiz.yaml
├── unit2_python_files/
│   ├── exercise1_first_py_file.py     # Actual Python files start here
│   ├── exercise2_run_from_terminal.py
│   ├── ... (all 8 exercises)
│   ├── quiz.yaml
│   └── graders/
│       ├── unit_grader.py
│       └── project_grader.py
└── final_exam.yaml
```

**Alternative Structure (More Traditional):**
- Create `.py` files for all units, but they contain instruction comments
- Students read comments, perform terminal/VSCode actions
- Can't auto-grade but maintains consistent file structure
- Consider which approach fits better with student expectations

## Success Criteria

Students completing Course 0 should be able to:
- Navigate the filesystem confidently using terminal
- Understand the concept of "current directory" and why it matters
- Use VSCode to create, edit, and save files
- Open VSCode's integrated terminal and understand its relationship to the file system
- Create Python files and run them from both terminal and VSCode
- Read basic error messages and debug simple syntax errors
- Feel comfortable experimenting without fear of "breaking something"

**Confidence Markers:**
- "I know how to find where I am in the terminal"
- "I can create and run a Python file without looking up instructions"
- "I understand what happens when I click the run button"
- "I can read an error message and figure out what's wrong"
- "I'm not scared of the terminal anymore"

This course is NOT about learning to code. It's about learning to operate the tools that let you code. Success means comfort and confidence, not mastery.
