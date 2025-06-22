#!/usr/bin/python3
import os

os.makedirs("python-everything_is_object", exist_ok=True)

answers = {
"0-answer.txt": "type",
"1-answer.txt": "id",
"2-answer.txt": "No",
"3-answer.txt": "Yes",
"4-answer.txt": "Yes",
"5-answer.txt": "No",
"6-answer.txt": "True",
"7-answer.txt": "True",
"8-answer.txt": "True",
"9-answer.txt": "True",
"10-answer.txt": "True",
"11-answer.txt": "False",
"12-answer.txt": "True",
"13-answer.txt": "True",
"14-answer.txt": "[1, 2, 3, 4]",
"15-answer.txt": "[1, 2, 3]",
"16-answer.txt": "1",
"17-answer.txt": "[1, 2, 3, 4]",
"18-answer.txt": "[1, 2, 3]",
"20-answer.txt": "Yes",
"21-answer.txt": "Yes",
"22-answer.txt": "No",
"23-answer.txt": "Yes",
"24-answer.txt": "True",
"25-answer.txt": "True",
"26-answer.txt": "True",
"27-answer.txt": "No",
"28-answer.txt": "Yes"
}

for filename, content in answers.items():
    path = os.path.join("python-everything_is_object", filename)
    with open(path, "w") as f:
        f.write(content + "\n")
    os.chmod(path, 0o755)

# File 19: Python file with header and 3-line content
py_file = os.path.join("python-everything_is_object", "19-copy_list.py")
with open(py_file, "w") as f:
    f.write("#!/usr/bin/python3\n")
    f.write("def copy_list(a_list):\n")
    f.write("    return a_list[:]\n")
os.chmod(py_file, 0o755)

# README.md
readme_path = os.path.join("python-everything_is_object", "README.md")
with open(readme_path, "w") as f:
    f.write("# Python - Everything is object\n")
os.chmod(readme_path, 0o644)
