from textual.app import App, ComposeResult
from textual.widgets import Button, Label

class ContentTest(App):
    def compose(self) -> ComposeResult:
        yield Label("[red][bold]Tex[not bold]tu[/]al[/bold][/] Rocks!")
        yield Label("[green]Python[/] for the win!")
        yield Button("exit")

    def on_button_pressed(self) -> None:
        self.app.exit()


if __name__ == "__main__":
    app = ContentTest()
    app.run()