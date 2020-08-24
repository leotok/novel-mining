# Dynamic relationship graph extraction in literary texts

## Data
- One Hundred Years of solitude, Gabriel G. Marquez (.txt file)

## Installing

```sh
$ pip install -r processing/requirements.txt
$ pip install -r graph_api/requirements.txt
$ python -m spacy download pt_core_news_sm
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

## How to use

After running both the backend and the frontend, access `localhost:3000` and you should see the following interface.

![alt text][https://github.com/leotok/novel-mining/raw/master/imgs/interface.png]


