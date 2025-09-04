# run_nano.py

from os import system

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button

class TextEditorApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Open Nano", id="nano")
        yield Button("Exit", id="exit")

    @on(Button.Pressed, "#exit")
    def terminate_application(self) -> None:
        self.exit()

    @on(Button.Pressed, "#nano")
    def run_nano(self) -> None:
        with self.suspend():
            system("nano")


if __name__ == "__main__":
    app = TextEditorApp()
    app.run()