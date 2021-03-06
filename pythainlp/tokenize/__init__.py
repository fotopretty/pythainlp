# -*- coding: utf-8 -*-
"""
Tokenizers at different level of linguistic analysis.
"""

__all__ = [
    "Tokenizer",
    "Trie",
    "sent_tokenize",
    "subword_tokenize",
    "syllable_tokenize",
    "word_tokenize",
]

from pythainlp.corpus import thai_syllables, thai_words
from pythainlp.util.trie import Trie

DEFAULT_WORD_TOKENIZE_ENGINE = "newmm"
DEFAULT_SENT_TOKENIZE_ENGINE = "crfcut"
DEFAULT_SUBWORD_TOKENIZE_ENGINE = "tcc"
DEFAULT_SYLLABLE_TOKENIZE_ENGINE = "dict"

DEFAULT_WORD_DICT_TRIE = Trie(thai_words())
DEFAULT_SYLLABLE_DICT_TRIE = Trie(thai_syllables())
DEFAULT_DICT_TRIE = DEFAULT_WORD_DICT_TRIE

from pythainlp.tokenize.core import (
    Tokenizer,
    sent_tokenize,
    subword_tokenize,
    syllable_tokenize,
    word_tokenize,
)
