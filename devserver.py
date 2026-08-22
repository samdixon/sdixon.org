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


@app.route('/404.html')
def not_found_page():
    """The 404 body, as a real page so Frozen-Flask writes build/404.html.

    CloudFront serves this key for 403/404 from the origin and rewrites the
    status back to 404 (see infra/site.yaml), so the status here must stay
    200 — Frozen-Flask refuses to freeze a non-200 response.
    """
    return render_template('404.html', context={})


@app.errorhandler(404)
def handle_404(_error):
    """Same page, real status, for the dev server. Not frozen — Frozen-Flask
    only walks registered URL rules, so this is dev-only sugar that keeps
    `make runserver` honest about what a miss looks like."""
    return render_template('404.html', context={}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
