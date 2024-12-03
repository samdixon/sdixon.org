import json
from typing import TypedDict, cast
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', context={})

@app.route("/about/")
def about():
    return render_template('about.html', context={'about': True})

class Hit(TypedDict):
    title: str
    blockquote: list[str]
    cite: str
    href: str
    

def parse_hits() -> list[Hit]:
    with open('data/hits.json') as f:
        hits = cast(list[Hit], json.loads(f.read()))
    return hits


@app.route('/hits/')
def hits():
    return render_template('hits.html', context={'hits': parse_hits(), 'hits_flag': True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
