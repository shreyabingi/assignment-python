import click
import ollama

@click.command()
@click.option('-t', '--text-file', type=click.Path(exists=True), help='Text file to summarize')
@click.argument('text', required=False)
def summarize(text_file, text):
    if text_file:
        with open(text_file, 'r') as file:
            content = file.read()
    elif text:
        content = text
    else:
        click.echo("Please provide either a text file or direct text input.")
        return

    try:
        response = ollama.chat(model='qwen2:0.5b', messages=[
            {
                'role': 'user',
                'content': f"Summarize the following text:\n\n{content}"
            }
        ])
        summary = response['message']['content']
        click.echo(f"Summary: {summary}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    summarize()