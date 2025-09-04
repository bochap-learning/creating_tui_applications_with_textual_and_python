from textual.app import App, ComposeResult
from textual.widgets import Button

class SimpleApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Exit")

    def on_button_pressed(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = SimpleApp()
    app.run()
