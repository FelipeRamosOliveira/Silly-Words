# Silly Words

Toolkit for descriptive text analysis: n-gram frequency counts and distribution charts on top of pandas, scikit-learn and seaborn.

## Structure

```sh
.
├── data/test_corpus.csv          # sample corpus
├── notebooks/                    # proofs of concept
├── sillywords
│   ├── text/words_counter.py     # NgramsCount
│   └── charts/dist_plot.py       # WordDistPlot
└── tests/
```

## Installation

Requires Python 3.9+ and [Poetry](https://python-poetry.org/).

```sh
poetry install
```

## Usage

```python
import pandas as pd
from sillywords.text.words_counter import NgramsCount
from sillywords.charts.dist_plot import WordDistPlot

corpus = pd.read_csv("data/test_corpus.csv")

# Top 20 bigrams of the "text" column
bigrams = NgramsCount(corpus, collum="text", nintens=2, rank=20)

WordDistPlot(bigrams, x="Bigram", y="Frequency", rank=20)
```

`NgramsCount` returns a DataFrame with the n-gram column (`Word`, `Bigram`, `Trigram` or `N_gram`) and `Frequency`, sorted by frequency.

## Tests

```sh
poetry run pytest
```
