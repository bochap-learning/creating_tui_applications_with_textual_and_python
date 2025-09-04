from typing import Iterable
from textual.widget import Widget
from textual.widgets import Button
from textual.app import App

class HelloStyleApp(App):
    def on_mount(self) -> None:
        self.screen.styles.background = "darkgreen"
        self.screen.styles.border = ("dashed", "yellow")

    def compose(self) -> Iterable[Widget]:
        yield Button("exit")

    def on_button_pressed(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = HelloStyleApp()
    app.run()