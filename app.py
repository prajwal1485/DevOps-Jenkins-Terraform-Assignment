
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary task storage
tasks = [
    {"id": 1, "title": "Learn Jenkins CI/CD", "completed": False},
    {"id": 2, "title": "Understand Terraform", "completed": False}
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")

    if title and title.strip():
        new_id = max([task["id"] for task in tasks], default=0) + 1

        tasks.append({
            "id": new_id,
            "title": title.strip(),
            "completed": False
        })

    return redirect(url_for("home"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

    return redirect(url_for("home"))

def reset_tasks():
    global tasks
    tasks = [
        {"id": 1, "title": "Learn Jenkins CI/CD", "completed": False},
        {"id": 2, "title": "Understand Terraform", "completed": False}
    ]

if __name__ == "__main__":
    app.run(debug=True)
