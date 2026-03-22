import random
import string
from pathlib import Path

Path("random_files").mkdir(exist_ok=True)

for i in range(10):
    name = ""
    for j in range(8):
        name = name + random.choice(string.ascii_letters + string.digits)
      
    file_path = Path("random_files") / (name + ".txt")
    file_path.touch()

    print(file_path.absolute())
