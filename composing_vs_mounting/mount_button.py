from textual.app import App, ComposeResult
from textual.widgets import Button

class WelcomeButton(App):
    def compose(self) -> ComposeResult:
        yield Button("Exit", id="exit")
        yield Button("Mount", id="mount")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit":
            self.exit()
        elif event.button.id == "mount":
            self.mount(Button("More"))

if __name__ == "__main__":
    app = WelcomeButton()
    app.run()
