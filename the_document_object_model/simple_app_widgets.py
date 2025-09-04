from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label

class SimpleApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("This is a simple label")
        yield Button("Exit")

    def on_button_pressed(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = SimpleApp()
    app.run()
