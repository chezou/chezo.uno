# pip install -r requirements.txt -c constraints.txt
from prelims import StaticSitePostsHandler
from prelims.processor import Recommender

tfidf_opts_en = {"stop_words": "english", "max_df": 0.95, "min_df": 2}
handler = StaticSitePostsHandler(r"content/blog", ignore_files=['_index.md'])
handler.register_processor(Recommender(permalink_base="/blog", **tfidf_opts_en))
handler.execute()

from sudachipy import tokenizer
from sudachipy import dictionary
from spacy.lang.ja.stop_words import STOP_WORDS

tokenizer_obj = dictionary.Dictionary(dict="full").create()
mode = tokenizer.Tokenizer.SplitMode.C

def tokenize(text):
    return [
        m.surface()
        for m in tokenizer_obj.tokenize(text, mode)
        if m.part_of_speech()[0] in ["名詞", "形容詞"] and 2 <= len(m.surface()) <= 15
    ]


tfidf_opts = {"tokenizer": tokenize, "stop_words": STOP_WORDS, "max_df": 0.95, "min_df": 2}

post_handler = StaticSitePostsHandler(r"content/post", ignore_files=['_index.md'])
post_handler.register_processor(Recommender(permalink_base="/post", **tfidf_opts))
post_handler.execute()
