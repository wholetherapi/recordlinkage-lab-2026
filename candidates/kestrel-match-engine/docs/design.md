# Kestrel Match Engine - design notes

## Matching model

Every field value is encoded with a sentence-embedding model and records are
compared by cosine similarity in the embedding space, which lets the matcher
link records that share no normalised key. A small logistic model is trained
on top of the similarity features to produce the final decision. In the
internal taxonomy this is a Learned-embedding-based design.

## Operational notes

- Batch size is controlled by the caller; the library keeps no global state.
- Scores are written to the output stream together with the rule/model version.
