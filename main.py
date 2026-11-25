import os

LINE = "I can control the weather, but only inside a one-inch cube directly above my left shoe."

try:
    os.makedirs("/output", exist_ok=True)
except OSError:
    pass

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
