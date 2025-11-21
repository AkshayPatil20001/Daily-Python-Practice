import os
import re

README_PATH = "README.md"
PROBLEMS_DIR = "problems"

def get_days_data():
    days = []
    if not os.path.exists(PROBLEMS_DIR):
        return days

    for folder in sorted(os.listdir(PROBLEMS_DIR)):
        if folder.startswith("day") and folder[3:].isdigit():
            day_number = int(folder[3:])
            folder_path = os.path.join(PROBLEMS_DIR, folder)

            py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]
            count = len(py_files)

            days.append({
                "day": day_number,
                "count": count,
                "path": f"problems/{folder}/"
            })

    return sorted(days, key=lambda x: x["day"], reverse=True)


def generate_table(days):
    table = "| Day | Problems Solved | Folder Link |\n"
    table += "| :---: | :---: | :---: |\n"

    for d in days:
        table += (
            f"| **Day {d['day']:03}** | {d['count']} | "
            f"[Day {d['day']} Solutions]({d['path']}) |\n"
        )

    return table


def update_readme(table):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"(<!-- PROGRESS-TABLE-START -->)(.*?)(<!-- PROGRESS-TABLE-END -->)"
    
    new_content = re.sub(
        pattern,
        r"\1\n" + table + r"\3",
        content,
        flags=re.DOTALL
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    days = get_days_data()
    table = generate_table(days)
    update_readme(table)
    print("README progress table updated successfully!")
    print("Detected days:", get_days_data())



if __name__ == "__main__":
    main()
