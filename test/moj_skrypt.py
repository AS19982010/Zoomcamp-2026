from pathlib import Path

current_dir = Path.cwd()
try:
    current_file = Path(__file__).name
except NameError:
    current_file = None

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if current_file and filepath.name == current_file:
        continue
    print(f"  - {filepath.name}")
    if filepath.is_file():
        try:
            content = filepath.read_text(encoding='utf-8')
            print(f"    Content: {content}")
        except:
            print(f"    (Cannot read this file)")
