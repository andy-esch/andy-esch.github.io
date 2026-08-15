# andyes.ch

Personal website of Andy Eschbacher: <https://andyes.ch>

The site is generated with the Hugo version pinned in `.hugo-version`. It intentionally has no theme, browser JavaScript, or Node/Ruby dependency.

Install the pinned standard Hugo binary with Go if it is not already available:

```sh
go install github.com/gohugoio/hugo@v$(cat .hugo-version)
```

Preview locally:

```sh
hugo server
```

Build and validate the exact GitHub Pages artifact:

```sh
hugo build --gc --minify
bash scripts/check-site.sh
```

Only `public/` is deployable. It is generated output and must not be edited or committed.
