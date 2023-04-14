from flask import Flask
import click

app = Flask(__name__)


@app.cli.command()
def ceshi():
    click.echo("自定义命令测试成功")
   
@app.cli.command()
def ls():
    click.echo("检查IP地址") 
    import os
    os.system("ping www.baidu.com")
    
if __name__ == "__main__":
    app.run()