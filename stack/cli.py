import typer

app = typer.Typer()


@app.command()
def stack():
    print("Hello world")


def main():
    app()
