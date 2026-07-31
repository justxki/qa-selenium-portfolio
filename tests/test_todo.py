import pytest

from pages.todo import ToDoList

@pytest.fixture
def todo():
    return ToDoList()


def test_todo_active_init(todo):
  assert todo.active == []

def test_todo_completed_init(todo):
  assert todo.completed == []

def test_todo_add(todo):
    todo.add("Hit the gym")
    assert todo.active == ["Hit the gym"]

def test_todo_add_two(todo):
    todo.add("Hit the gym")
    todo.add("Eat dinner early.")
    assert todo.active == ["Hit the gym", "Eat dinner early."]

def test_todo_add_dupe(todo):
    todo.add("Hit the gym")
    with pytest.raises(ValueError):
        todo.add("Hit the gym")

### def test_todo_add_empty_str(todo):
###     with pytest.raises(ValueError):
###         todo.add("")

def test_todo_remove(todo):
    todo.add("Drink more water")
    todo.remove("Drink more water")
    assert todo.active == []

def test_todo_remove_two(todo):
    todo.add("Drink more water")
    todo.add("Read motivation book")
    todo.add("5pm nap")
    todo.remove("5pm nap")
    todo.remove("Drink more water")
    assert todo.active == ["Read motivation book"]

### def test_todo_remove_notonemptylist(todo):
###     with pytest.raises(ValueError):
###         todo.remove("Go hiking this week.")

def test_todo_remove_notonlist(todo):
    todo.add("Go hiking next week.")
    with pytest.raises(ValueError):
        todo.remove("Go hiking this week.")

### def test_todo_remove_empty_str(todo):
###    with pytest.raises(ValueError):
###         todo.remove("")

def test_todo_complete(todo):
    todo.add("Drink more water")
    todo.complete("Drink more water")
    assert todo.completed == ["Drink more water"]

def test_todo_complete_two(todo):
    todo.add("Read motivation book")
    todo.add("5pm nap")
    todo.complete("Read motivation book")
    todo.complete("5pm nap")
    assert todo.completed == ["Read motivation book", "5pm nap"]

### def test_todo_complete_notonemptylist(todo):
###     with pytest.raises(ValueError):
###     todo.complete("Go hiking this week.")

def test_todo_complete_notonlist(todo):
    todo.add("Go hiking next week.")
    with pytest.raises(ValueError):
        todo.complete("Go hiking this week.")

def test_todo_add_complete_remove(todo):
    todo.add("Go hiking next week.")
    todo.complete("Go hiking next week.")
    with pytest.raises(ValueError):
        todo.remove("Go hiking next week.")

def test_todo_add_complete_both_lists(todo):
    todo.add("Study math")
    todo.add("Mow the lawn thurs")
    todo.complete("Mow the lawn thurs")
    assert todo.active == ["Study math"]
    assert todo.completed == ["Mow the lawn thurs"]

### def test_todo_complete_empty_str(todo):
###     with pytest.raises(ValueError):
###         todo.complete("")

#def test_todo_complete_dupe(todo):
#    todo.add("Hit the gym")
#    with pytest.raises(ValueError):
#        todo.add("Hit the gym")
    #narcissist dev route no double complete protection
#wait nvm this won't happen bc we coded .add to not save duplicates. so .complete can never grab dupes.
#if there was a way i could test it anyways as a "just in case" like a Qa person would, i would, but it would crash first.


one_step_errors = [
    ("add", ""),
    ("remove", "Go hiking this week."),
    ("remove", ""),
    ("complete", "Go hiking this week."),
    ("complete", ""),
]

@pytest.mark.parametrize("method_name, error_str", one_step_errors)
def test_error_raise_error_str(todo, method_name, error_str):
    bad_method = getattr(todo, method_name)
    with pytest.raises(ValueError):
        bad_method(error_str)