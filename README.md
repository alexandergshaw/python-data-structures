# Python Data Structures — Course Repository

Welcome! This guide explains the complete GitHub workflow you will follow every time you submit an assignment: creating a branch, opening a Codespace, making and saving changes, opening a Pull Request, and merging your work.

---

## GitHub Workflow — Step by Step

### Step 1: Create a Branch

A branch is your own personal copy of the repository where you can make changes safely, without affecting anyone else's work.

1. Go to the repository on **GitHub.com**.
2. Click the **branch selector dropdown** near the top-left of the page (it shows `main` by default).
3. In the text box that appears, type a name for your new branch using the format `module-XX-yourname` (e.g., `module-01-alex`).
4. Click **"Create branch: module-01-alex from 'main'"**.
5. GitHub switches you to your new branch automatically — confirm by checking the branch dropdown.

> **Why branches?** They keep your work isolated. If something goes wrong, `main` stays clean and you can always start a fresh branch.

---

### Step 2: Open a Codespace on Your Branch

GitHub Codespaces gives you a full Visual Studio Code environment running in the cloud — no local installation required.

1. Make sure the branch dropdown shows **your branch name** (not `main`).
2. Click the green **`<> Code`** button near the top-right of the page.
3. Select the **`Codespaces`** tab in the dropdown.
4. Click **"Create codespace on \<your-branch-name\>"**.
5. A new browser tab opens with VS Code loading. Wait 1–2 minutes for setup to finish.

> **Tip:** If you close the Codespace tab by accident, you can reopen it from the same **`<> Code → Codespaces`** menu — your work is still there.

---

### Step 3: Make Your Changes

1. In the Codespace, open the **Explorer panel** on the left (`Ctrl+Shift+E` / `Cmd+Shift+E`).
2. Navigate to the module folder for your assignment (e.g., `assignments/module_01/`).
3. Right-click the folder and select **"New File"**, then type the filename your assignment specifies (e.g., `basics.py`).
4. Write your code. Save the file with `Ctrl+S` / `Cmd+S` at any time.

---

### Step 4: Stage Your Changes

Staging tells Git exactly which files you want to include in your next save-point (commit).

1. Click the **Source Control icon** in the left sidebar (branching-tree icon, or `Ctrl+Shift+G` / `Cmd+Shift+G`).
2. Under **"Changes"**, you will see your modified or new files listed.
3. Click the **`+`** (Stage Changes) icon next to each file you want to include, **or** click the **`+`** next to "Changes" to stage everything at once.
4. The files move to a **"Staged Changes"** section.

> **Why stage?** It lets you group related changes into one logical commit, even if you have edited multiple files.

---

### Step 5: Commit Your Changes

A commit is a permanent snapshot of your staged changes, labeled with a message describing what you did.

1. In the **"Message"** box at the top of the Source Control panel, type a short, descriptive message (e.g., `Add module 01 basics exercise`).
2. Click the **✓ Commit** button (or press `Ctrl+Enter` / `Cmd+Enter`).
3. Your changes are now saved locally in the Codespace.

> **Good commit messages** start with a verb and describe *what* changed: `Add`, `Fix`, `Update`, `Remove`.

---

### Step 6: Push Your Changes to GitHub

Pushing sends your local commit(s) from the Codespace to your branch on GitHub.com.

1. After committing, a **"Sync Changes"** button (or cloud/upload icon) appears in the Source Control panel.
2. Click **"Sync Changes"** to push.
3. If prompted to confirm, click **OK**.
4. Go back to GitHub.com, switch to your branch, and verify your files appear there.

---

### Step 7: Open a Pull Request (PR)

A Pull Request asks a reviewer (your instructor) to look at your work and approve merging it into `main`.

1. On GitHub.com, you will see a yellow banner saying **"Your branch had recent pushes"** — click **"Compare & pull request"**.
   - If the banner is gone, go to the **Pull requests** tab and click **"New pull request"**. Set the base branch to `main` and your branch as the compare branch.
2. Give your PR a clear title (e.g., `Module 01 Submission — Alex`).
3. In the description box, briefly describe what you completed.
4. Click **"Create pull request"**.
5. Your instructor will review your code and leave comments or approve it.

---

### Step 8: Merge Your Pull Request

Once your instructor approves the PR, you can merge your branch into `main`.

1. On the PR page, click **"Merge pull request"**.
2. Click **"Confirm merge"**.
3. Optionally click **"Delete branch"** to clean up after yourself.

> **Congratulations — your work is now part of `main`!**

---

## Repository Structure

```
python-data-structures/
├── README.md                  ← You are here — workflow guide
└── assignments/
    ├── README.md              ← Assignment index
    ├── module_01/             ← Week 1: Python Basics I
    ├── module_02/             ← Week 2: Python Basics II
    ├── module_03/             ← Week 3: Functions and Collections
    ├── module_04/             ← Week 4: Complexity Analysis
    ├── module_05/             ← Week 5: Object-Oriented Programming
    ├── module_06/             ← Week 6: Linked Lists
    ├── module_07/             ← Week 7: Stacks and Queues
    ├── module_08/             ← Week 8: Recursion
    ├── module_09/             ← Week 9: Searching and Sorting
    ├── module_10/             ← Week 10: Trees
    ├── module_11/             ← Week 11: Heaps and Priority Queues
    ├── module_12/             ← Week 12: Hash Tables
    ├── module_13/             ← Week 13: Graphs
    ├── module_14/             ← Week 14: Algorithmic Paradigms
    ├── module_15/             ← Week 15: Dynamic Programming
    └── module_16/             ← Week 16: Final Capstone
```

Each module folder contains a `README.md` with a detailed introduction to that week's concepts, examples, and hints to help you complete the assignment.
