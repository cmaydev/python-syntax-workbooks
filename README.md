# Python Syntax Workbooks (Reps → Solve → Refactor)

This repo is a typing-first Python training system.

You don’t “watch a tutorial.” You **type code** and you **prove it works** with tests.

Each lesson is a 3-page micro-cycle:

1) **REPS** (Page 1): Type the given function **10x** to lock in syntax + patterns.
2) **SOLVE** (Page 2): Use the same pattern to solve a prompt from scratch.
3) **REFACTOR** (Page 3): Improve readability (“pythonic”) without changing behavior.

Tests are split per page so you always get clean pass/fail feedback.

---

## Requirements

- Python 3.11+ recommended
- VS Code
- (Optional but recommended) Git

---

## VS Code settings (training mode)

Turn off “helpful” autocomplete so you’re actually training.

In VS Code Settings:
- Disable: **Editor: Inline Suggest Enabled**
- Disable: **Editor: Suggest On Trigger Characters**
- Optional: set **Accept Suggestion On Enter** = Off

Tip: create a dedicated VS Code “Profile” named `Python Training` so you can switch back to normal dev mode later.

---

## Setup (Windows / PowerShell)

From repo root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt