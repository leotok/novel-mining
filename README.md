# Novel Mining

## Data (.txt file)
- One Hundred Years of solitude, Gabriel G. Marquez

## Installing

```sh
$ pip install -r processing/requirements.txt
$ pip install -r graph_api/requirements.txt
```

## Testing

```sh
$ python -m unittest
```

## Running the text processing script

```sh
$ PYTHONPATH=. python processing/book_processing.py
```

## Running the Graph API

```sh
$ PYTHONPATH=. python graph_api/app.py
```

## Running the Graph UI
```sh
$ cd relationship-graph-viewer
$ yarn
$ yarn start
```

