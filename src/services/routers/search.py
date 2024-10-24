import gensim.downloader as api
import numpy as np

from fastapi import APIRouter, HTTPException
from scipy.spatial.distance import cosine
from ..models.search import Sentence


router = APIRouter(
    prefix="/search-engine"
)

# globals
SENTENCES = [
    Sentence(sentence="Mark Zuckerberg owns Facebook"),
    Sentence(sentence="Jeff Bezos owns Amazon"),
    Sentence(sentence="Microsoft is owned by Bill Gates"),
    Sentence(sentence="Gorillas eat tons of bananas")
]


@router.post("/search")
def search(search: Sentence):
    global SENTENCES

    result = [
        i for i in SENTENCES
        if search.sentence.lower() in i.sentence.lower()
    ]
    if not result:
        raise HTTPException(status_code=404, detail="Sentence not found")
    return result


def get_vector(sentence: str, model):
    words = sentence.split()
    words = [w.lower() for w in words]
    vectors = np.array([model[w] for w in words if w in model])
    vector = np.sum(vectors, axis=0)
    return vector


def search_embeddings(search: str):
    global SENTENCES
    model = api.load("glove-wiki-gigaword-50")
    vector_search = get_vector(search)
    vectors = [get_vector(s.sentence, model) for s in SENTENCES]
    results = []
    for idx, v in enumerate(vectors):
        dist = cosine(vector_search, v)
        results.append((f"{SENTENCES[idx].sentence}", (1 - dist)))

    return sorted(results, key=lambda x: x[1], reverse=True)


@router.post("/smart_search")
def smart_search(search: Sentence):
    result = search_embeddings(search.sentence)
    return [
        {'sentence': r[0], 'score': r[1]} for r in result
    ]
