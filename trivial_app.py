# import os

from flask import Flask


def create_app(config_name):
    app = Flask(__name__)

    @app.route('/')
    def index():
        html = '''
           <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome to CircleCI2.0</title>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js"></script>
    </head>

    <style id="compiled-css" type="text/css">
        body {
            background: #FFF;
            padding: 20px;
            font-family: Helvetica;
        }
        button {
            background: #0084ff;
            border: none;
            border-radius: 5px;
            padding: 8px 14px;
            font-size: 15px;
            color: #fff;
        }
        .hidden {
            display: none;
        }
        .show {
            display: block;
        }
    </style>

    <script type="text/javascript">
        window.onload=function(){
            var text = $("#text")
            var button = $("#button")
            button.on("click", function(){
                text.addClass("show");
                text.removeClass('hidden');
            })
        }
    </script>

    <body>

    <div class="container">
        <h1>Welcome to CircleCI2.0</h1>

        <button id='button'>Click ME!</button>

        <h2 id='text' class="hidden">Hello World!! Welcome!</h2>
    </div>


    </body>
    </html>'''
        return html
    return app
