class Task:
    def __init__(self, description, due_date, is_done=False):
        self.description = description
        self.due_date = due_date
        self.is_done = is_done

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"'{self.description}', срок: {self.due_date}, статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                print(f"Задача '{description}' была отмечена как выполненная.")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    def show_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task.is_done:
                print(task)

manager = TaskManager()

manager.add_task(Task("Купить молоко", "01-05-2023"))
manager.add_task(Task("Записаться в спортзал", "01-06-2023"))
manager.add_task(Task("Позвонить другу", "05-05-2023"))

manager.show_current_tasks()

manager.mark_task_done("Купить молоко")

manager.show_current_tasks()