---
trigger: always_on
---

# Python Execution Rule

- 在此專案中執行任何 Python 指令、腳本或套件管理工具（如 `python`、`pip`、`pytest` 等）時，**一律使用專案根目錄下的虛擬環境 (`venv`)**，不可直接使用系統全域的 Python。
- Windows 環境請使用：`.\venv\Scripts\python.exe`（以及 `.\venv\Scripts\pip.exe`）
- macOS / Linux 環境請使用：`./venv/bin/python`（以及 `./venv/bin/pip`）
