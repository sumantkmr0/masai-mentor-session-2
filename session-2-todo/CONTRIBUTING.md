# Contributing Guide: Git Best Practices

Welcome! This guide teaches you professional Git workflow practices that you'll use throughout your career as a developer.

## 🎯 What You'll Learn

This isn't just about completing exercises - it's about learning to work like professional developers:

- **Version Control**: Track every change you make
- **Save Early, Save Often**: Never lose your work
- **Meaningful Commits**: Help others understand your changes
- **Code Organization**: Keep your project clean and structured
- **Documentation**: Make your code understandable

---

## 📋 The Complete Workflow

### Step 1: Fork the Repository

**What is Forking?**
Forking creates your own personal copy of the project on GitHub where you can make changes without affecting the original.

**How to Fork:**
1. Click the "Fork" button at the top-right of the repository page
2. GitHub will create a copy under your account
3. You now have your own version to work with!

**Why Fork?**
- You can experiment freely
- Changes don't affect the original project
- You can submit your changes back via Pull Request

---

### Step 2: Clone Your Fork

**What is Cloning?**
Cloning downloads the code from GitHub to your computer so you can work on it locally.

```bash
# Replace YOUR-USERNAME with your actual GitHub username
git clone https://github.com/YOUR-USERNAME/python-week2-workshop
cd python-week2-workshop
```

**Verify you're in the right place:**
```bash
pwd  # Shows your current directory
ls   # Lists files in the directory
```

You should see: `README.md`, `exercises/`, `tests/`, etc.

---

### Step 3: Create a Branch

**What is a Branch?**
A branch is like a parallel version of your code where you can make changes safely without affecting the main code.

```bash
git checkout -b fix-bugs
```

**Branch Naming Conventions:**
- Use descriptive names: `fix-bugs`, `add-greeting-feature`, `update-calculator`
- Use hyphens, not spaces: `fix-bugs` ✅, not `fix bugs` ❌
- Keep it concise but clear

**Why Use Branches?**
- Keep your main branch clean
- Work on multiple features separately
- Easy to abandon changes if needed
- Professional standard practice

**Check your current branch:**
```bash
git branch
# * fix-bugs  ← The asterisk shows your current branch
```

---

### Step 4: Make Changes & Test

**The Development Cycle:**

1. **Read the exercise instructions carefully**
2. **Make a small change** (don't try to fix everything at once!)
3. **Test your change:**
   ```bash
   python exercises/calculator.py
   ```
4. **If it works, move to the next change**
5. **If it doesn't work, read the error message and fix it**

**💡 Best Practice: "Save Early, Save Often"**

Don't wait until everything is perfect! Make small, frequent commits. Here's why:

- ✅ Easy to identify what caused a bug
- ✅ Can undo specific changes if needed
- ✅ Shows clear progress
- ✅ Prevents losing hours of work

---

### Step 5: Stage Your Changes

**What is Staging?**
Staging selects which changes you want to include in your next commit.

**Check what files changed:**
```bash
git status
```

You'll see output like:
```
Changes not staged for commit:
  modified:   exercises/calculator.py
```

**Stage specific files:**
```bash
# Stage one file
git add exercises/calculator.py

# Stage multiple files
git add exercises/calculator.py exercises/greeting.py

# Stage all changed files (use carefully!)
git add .
```

**Best Practice: Stage Related Changes Together**
- ✅ Fixed calculator bugs? Stage calculator.py
- ✅ Completed greeting functions? Stage greeting.py in a separate commit
- ❌ Don't mix unrelated changes in one commit

---

### Step 6: Commit Your Changes

**What is a Commit?**
A commit is a snapshot of your code at a specific point in time with a description of what changed.

**Basic commit:**
```bash
git commit -m "Fix subtract function in calculator"
```

**Best Practice: Write Good Commit Messages**

**Good commit messages:**
```bash
git commit -m "Fix subtract function to use subtraction instead of addition"
git commit -m "Complete create_greeting and create_goodbye functions"
git commit -m "Fix grade calculation logic for C and D grades"
git commit -m "Add input validation to divide_numbers function"
```

**Bad commit messages:**
```bash
git commit -m "fix"  # Too vague
git commit -m "asdfgh"  # Meaningless
git commit -m "Updated files"  # Doesn't say what changed
git commit -m "Final version"  # Not descriptive
```

**Commit Message Format:**

```
[Action] [What you changed] [Why if not obvious]

Examples:
- Fix: Corrected subtract function operator
- Add: Implement multiply_numbers function
- Update: Improve error handling in divide_numbers
- Refactor: Simplify grade calculation logic
```

**Common Action Words:**
- **Fix**: Correcting a bug
- **Add**: Adding new functionality
- **Update**: Modifying existing functionality
- **Remove**: Deleting code or files
- **Refactor**: Restructuring code without changing behavior
- **Test**: Adding or modifying tests
- **Docs**: Updating documentation

---

### Step 7: Check Your Commit History

**View your commits:**
```bash
git log
```

**View commits in a simple format:**
```bash
git log --oneline
```

You'll see:
```
7a2d4f3 Fix grade calculation logic
5b8e2a1 Complete greeting functions
3c9f1d2 Fix subtract function
```

**What makes a good commit history?**
- Each commit represents one logical change
- Commit messages clearly describe what changed
- Easy to understand the project's evolution
- Makes debugging easier (you can identify when bugs were introduced)

---

### Step 8: Push Your Changes

**What is Pushing?**
Pushing uploads your local commits to GitHub so others can see them.

```bash
# First time pushing this branch
git push -u origin fix-bugs

# Subsequent pushes
git push
```

**What happens when you push?**
1. Your commits upload to GitHub
2. Your fork is updated
3. Others can now see your changes
4. You can create a Pull Request

**Troubleshooting Push Issues:**

**"Permission denied":**
- Make sure you're pushing to YOUR fork, not the original repository
- Check: `git remote -v`

**"Updates were rejected":**
- Someone else changed the code first
- Pull the latest changes: `git pull origin fix-bugs`
- Then push again: `git push`

---

### Step 9: Create a Pull Request (PR)

**What is a Pull Request?**
A Pull Request asks the original repository to "pull" your changes and merge them in.

**How to Create a PR:**

1. Go to YOUR fork on GitHub
2. You'll see a banner: "Compare & pull request" - click it
3. Fill in the PR description:

```markdown
## What I Fixed

- Fixed calculator subtraction bug (was using + instead of -)
- Completed all greeting functions with proper string formatting
- Fixed student grade logic errors (C and D were swapped)

## Testing Done

✅ All local tests pass
✅ Manually tested each function with various inputs
✅ Verified edge cases (division by zero, etc.)

## What I Learned

- Importance of reading error messages carefully
- How to use string concatenation properly
- Why testing edge cases matters
```

4. Click "Create pull request"
5. Watch the automated tests run!

**What makes a good PR description?**
- Clear summary of changes
- List of what was fixed/added
- Any testing you did
- Screenshots if relevant
- Questions if you're unsure about something

---

### Step 10: Respond to Feedback

**When Tests Fail:**
1. Don't panic! This is normal and expected
2. Read the error messages - they tell you exactly what's wrong
3. Fix the issues locally
4. Commit and push the fixes
5. Tests will run automatically again

```bash
# Fix the issue in your code
# Then:
git add exercises/calculator.py
git commit -m "Fix division by zero handling"
git push
```

**When Reviewers Comment:**
- Read comments carefully
- Ask questions if something is unclear
- Make requested changes
- Thank reviewers for their time
- Learn from the feedback!

---

## 🛠️ Essential Git Commands Reference

### Checking Status
```bash
git status              # See what files changed
git diff                # See exact changes in files
git log                 # View commit history
git log --oneline       # View compact commit history
git branch              # See all branches
```

### Making Changes
```bash
git add <file>          # Stage a specific file
git add .               # Stage all changed files
git commit -m "message" # Commit staged changes
git push                # Push commits to GitHub
```

### Branch Management
```bash
git checkout -b <name>  # Create and switch to new branch
git checkout <name>     # Switch to existing branch
git branch -d <name>    # Delete a branch (after merging)
```

### Undoing Changes
```bash
git checkout -- <file>  # Discard changes in a file
git reset HEAD <file>   # Unstage a file
git reset --soft HEAD~1 # Undo last commit (keep changes)
git reset --hard HEAD~1 # Undo last commit (discard changes)
```

### Getting Latest Changes
```bash
git pull                # Get latest changes from GitHub
git fetch               # Download changes without merging
```

---

## 📝 Code Quality Best Practices

### File Organization

```
project/
├── README.md              # Project overview and instructions
├── CONTRIBUTING.md        # This file - how to contribute
├── exercises/             # Exercise files students work on
│   ├── calculator.py
│   ├── greeting.py
│   └── student_info.py
├── tests/                 # Basic tests students can run
│   └── test_*.py
├── hidden_tests/          # Advanced tests (revealed in PR)
│   └── test_*_advanced.py
└── solutions/             # Reference solutions
    └── *_solution.py
```

**Why This Organization?**
- Easy to find files
- Clear separation of concerns
- Professional structure
- Scalable for larger projects

### Code Comments

**When to Comment:**

```python
# ✅ Good: Explains WHY
# Convert age to string because we can't concatenate int with str
return "My name is " + name + " and I am " + str(age) + " years old."

# ✅ Good: Explains complex logic
# Check if b is zero to prevent division error
if b == 0:
    return None

# ❌ Bad: States the obvious
x = 5  # Set x to 5

# ❌ Bad: Outdated comment
# Calculate average of two numbers
total = num1 + num2 + num3  # Actually three numbers!
```

**Docstrings (Function Documentation):**

```python
def calculate_average(num1, num2, num3):
    """
    Calculate the average of three numbers.

    Args:
        num1 (float): First number
        num2 (float): Second number
        num3 (float): Third number

    Returns:
        float: The average of the three numbers

    Example:
        >>> calculate_average(10, 20, 30)
        20.0
    """
    total = num1 + num2 + num3
    return total / 3
```

### Naming Conventions

**Functions:**
```python
# ✅ Good: Descriptive, uses verb, snake_case
def calculate_average(numbers):
def get_student_grade(score):
def is_passing(score):

# ❌ Bad: Vague, no verb, poor formatting
def calc(n):
def grade(x):
def PassCheck(s):
```

**Variables:**
```python
# ✅ Good: Descriptive, snake_case
student_score = 95
total_attendance = 20
is_eligible = True

# ❌ Bad: Single letters, unclear meaning
s = 95
ta = 20
x = True
```

**Constants:**
```python
# ✅ Good: All caps, descriptive
MAX_SCORE = 100
PASSING_GRADE = 60
DEFAULT_ATTENDANCE = 20

# ❌ Bad: Mixed case, unclear
Max_Score = 100
pg = 60
```

---

## 🎓 Learning Objectives

By following these practices, you're learning:

### Version Control Skills
- ✅ How to track changes over time
- ✅ How to collaborate with others
- ✅ How to maintain code history
- ✅ How to work on features in parallel

### Professional Workflow
- ✅ Writing clear commit messages
- ✅ Creating meaningful pull requests
- ✅ Responding to code reviews
- ✅ Testing before submitting

### Code Organization
- ✅ Structuring projects logically
- ✅ Writing clear documentation
- ✅ Following naming conventions
- ✅ Commenting effectively

### Problem-Solving
- ✅ Reading and understanding error messages
- ✅ Testing incrementally
- ✅ Debugging systematically
- ✅ Learning from failures

---

## ❓ Common Questions

**Q: How often should I commit?**
A: Commit whenever you complete a logical piece of work. For this workshop:
- After fixing each buggy function
- After completing each exercise file
- Before trying something experimental

**Q: What if I mess up?**
A: Git is very forgiving! Most mistakes can be undone. Ask for help if needed.

**Q: Should I commit code that doesn't work?**
A: For this workshop, try to commit working code. But in real projects, it's sometimes okay to commit work-in-progress with a clear message like "WIP: Adding feature X".

**Q: Can I delete my commits?**
A: Yes, but be careful! Commits that have been pushed to GitHub and seen by others shouldn't be deleted.

**Q: What if my tests fail?**
A: Read the error messages carefully - they tell you exactly what's wrong! Fix the issues and push again.

---

## 🚀 Next Steps

After mastering these basics:

1. **Learn about branches**: Create feature branches for each new task
2. **Explore Git history**: Use `git log`, `git diff`, `git blame`
3. **Practice rebasing**: Clean up your commit history
4. **Resolve merge conflicts**: Handle concurrent changes
5. **Use Git hooks**: Automate checks before committing

---

## 📚 Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Commit Message Guidelines](https://chris.beams.io/posts/git-commit/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

---

## 💡 Remember

> "The best time to start using version control was when you started coding. The second best time is now."

Good habits learned now will serve you throughout your entire career!

**Happy coding!** 🎉
