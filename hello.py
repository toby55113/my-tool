import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("環境測試成功")
print(f"Python 版本: {sys.version}")
