from flask import Flask , request , render_template

app = Flask(__name__)

@app.route("/")
def introduce():
    from .data.about import bot
    return render_template("index.html",data=bot,question={'key':"name","text":"what is ur name..🤗"})

@app.route("/message", methods=['POST'])
def user_message():
    if request.method == 'POST':
        from .intents import handle
        return handle(request.form)
    else:
        return "OOPS.. INVLAID"