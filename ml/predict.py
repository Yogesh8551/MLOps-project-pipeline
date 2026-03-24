file_test_map = {
    "models.py": ["test_create.py", "test_get.py"],
    "main.py": ["test_complete.py"]
}

selected_tests = []

with open("changed_files.txt") as f:
    files = f.read().splitlines()

for file in files:
    for key in file_test_map:
        if key in file:
            selected_tests.extend(file_test_map[key])

selected_tests = list(set(selected_tests))

if not selected_tests:
    selected_tests = ["test_create.py"]

with open("tests_to_run.txt", "w") as f:
    for t in selected_tests:
        f.write(t + "\n")

print(selected_tests)