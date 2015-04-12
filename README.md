# ServerMap [![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

Resource monitoring tool for servers.

## Developing

### setup

`$ direnv edit .` → type `layout python`

## test

`$ nosetests`

### packaging

#### test

upload: `python setup.py sdist upload -r https://testpypi.python.org/pypi`

install: `pip install --index-url https://testpypi.python.org/simple/ servermap`

#### production

`python setup.py register`
`python setup.py sdist upload`
