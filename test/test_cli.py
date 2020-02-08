import click

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    return 'Service is runing...'

@app.cli.command('hello')
@click.option('--name', default='World')
def hello_command(name):
    # click.echo(f'Hello, {name}!')
    pass

def test_hello():
    runner = app.test_cli_runner()

    # invoke the command directly
    result = runner.invoke(hello_command, ['--name', 'Flask'])
    assert 'Hello, Flask' in result.output

    # or by name
    result = runner.invoke(args=['hello'])
    assert 'World' in result.output


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)


