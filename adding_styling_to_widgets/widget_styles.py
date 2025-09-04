# widget_styles.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label

class WidgetApp(App):
    def compose(self) -> ComposeResult:
        self.label = Label("Python")
        self.button = Button("Exit")
        yield self.label
        yield self.button

    def on_mount(self):
        self.label.styles.background = "pink"
        self.label.styles.border = ("heavy", "purple")
        self.button.styles.background = "aqua"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit()

if __name__ == "__main__":
    app = WidgetApp()
    app.run()