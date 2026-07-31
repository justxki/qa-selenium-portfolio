import pytest

from pages.tog import Toggle

@pytest.fixture
def tog():
    return Toggle()

def test_init_state(tog):
    assert tog.state == False

def test_flip_changes_state(tog):
    tog.flip()
    assert tog.state == True

def test_flip_changes_state_double(tog):
    tog.flip()
    tog.flip()
    assert tog.state == False

def test_flip_changes_state_triple(tog):
    tog.flip()
    tog.flip()
    tog.flip()
    assert tog.state == True

def test_flip_after_turn_on(tog):
    tog.turn_on()
    tog.flip()
    assert tog.state == False

def test_flip_after_turn_off(tog):
    tog.turn_on()
    tog.turn_off()
    tog.flip()
    assert tog.state == True

def test_turn_on_after_flip(tog):
    tog.flip()
    with pytest.raises(ValueError):
        tog.turn_on()

def test_turn_off_after_flip(tog):
    tog.flip()
    tog.turn_off()
    assert tog.state == False

def test_turn_on_works(tog):
    tog.turn_on()
    assert tog.state == True

def test_turn_on_when_already_on_raises(tog):
    tog.turn_on()
    with pytest.raises(ValueError):
        tog.turn_on()

def test_turn_off_works(tog):
    tog.turn_on()
    tog.turn_off()
    assert tog.state == False

def test_turn_off_when_already_off_raises(tog):
    with pytest.raises(ValueError):
        tog.turn_off()