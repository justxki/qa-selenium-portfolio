class ToDoList:
    def __init__(self):
        self._active = []
        self._completed = []

    @property
    def active(self):
        return self._active

    @property
    def completed(self):
        return self._completed

        # your call: what if task is empty string? what if it's already in the list?
    def add(self, task):
        if task == "":
            raise ValueError("Must type something to add to list")
        if task in self._active:
            raise ValueError("Task already in list")
        self._active.append(task)

    def remove(self, task):
        if task not in self._active:
            raise ValueError(f"Task not on list. Must type a task on your list to remove from list. Here is your list:\n{self._active}")
        if task == "":
            raise ValueError(f"Must type a task on your list to remove from list. Here is your list:\n{self._active}")
        self._active.remove(task)


    def complete(self, task):
        # move from active to completed
        # your call: what if not in active? what if already completed?
        if task not in self._active:
            raise ValueError(f"Task not on list. Must type a task on your list to complete the task. Here is your list:\n{self._active}")
        if task == "":
            raise ValueError(f"Must type a task on your list to complete the task. Here is your list:\n{self._active}")
        self._active.remove(task)
        self._completed.append(task)

#todo = ToDoList()
#todo.add("Go swim.")
#print(todo)
#todo.remove("Go hiking.")
#print(todo)