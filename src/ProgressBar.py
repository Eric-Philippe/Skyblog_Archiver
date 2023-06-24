"""
This file contains the ProgressBar class, which is used to display a progress bar
in the console
"""
class ProgressBar(object):
    def __init__(self, total: int):
        self.total = total
        self.size = 20
        self.progress = 0
        self.bar = ["."] * self.size
        self.bar = "[" + "".join(self.bar) + "]"
        self.status = "0% 0/" + str(self.total)

    """
    Display the progress bar
    """
    def display(self):
        print("\033[K", end="")
        # If the progress is 100%, print in green, else print in yellow
        if self.progress == self.total:
            print("\033[32m", end="")
        else:
            print("\033[33m", end="")
        print(f"\rProgress: {self.bar} {self.status}", end="")

    """
    Update the progress bar
    """
    def update(self, progress: int):
        self.progress = progress
        self.update_bar()
        self.update_status()
        self.display()

    """
    Update the bar
    """
    def update_bar(self):
        progress = int((self.progress / self.total) * self.size)
        remaining = self.size - progress
        self.bar = "[" + "#" * progress + "." * remaining + "]"

    """
    Update the status
    """
    def update_status(self):
        percentage = round((self.progress / self.total) * 100, 2)
        self.status = f"{percentage}% {self.progress}/{self.total}"
