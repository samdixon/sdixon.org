## sdixon.org

static site for sdixon.org

## setup
Requires [uv](https://docs.astral.sh/uv/). Dependencies are pinned in `uv.lock`.
```
make sync
```
`uv` also installs the right Python (see `.python-version`) if it isn't already present.

`requirements.txt` is generated from `uv.lock` (for the cloudflare pages build, which
installs with pip) and is committed. Regenerate it after changing dependencies:
```
make requirements
```

## running locally
```
make runserver
```

## building locally
```
make build
```

## remote dev
* push to new branch and automatically deploy a preview branch via cloudflare pages.

* when ready, merge to main
