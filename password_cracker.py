from zipfile import ZipFile

# Load all passwords from leak
with open('img/Ashley-Madison.txt', 'r', encoding='latin-1') as f:
    passwords = [line.rstrip('\n') for line in f]

print(f"Loaded {len(passwords)} passwords. Starting crack...")

for i, password_str in enumerate(passwords):
    if i % 10000 == 0:
        print(f"Iteration {i}: trying '{password_str}'")

    password = password_str.encode('latin-1')

    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            zf.extractall(pwd=password)
        print(f"\nPassword found: {password_str}")
        break
    except Exception:
        continue
