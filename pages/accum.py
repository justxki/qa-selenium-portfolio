class Accumulator:
    def __init__(self):
        # THE PAPER: The actual hidden number.
        # (The underscore before _count is a Python convention that means "private, keep your hands off")
        self._count = 0

    @property
    def count(self) -> int:
        # THE GLASS WINDOW: Lets you look at the paper safely without parens.
        return self._count #(no parenths, not calling anything remember girl)

    def add(self, more=1) -> None:
        # THE BUTTON: The only allowed way to change the number on the paper.
        self._count += more