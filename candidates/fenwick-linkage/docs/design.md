# Fenwick Linkage - design notes

## Matching model

The pair scorer produces a composite similarity for every candidate pair.
Fenwick Linkage then builds a weighted similarity graph: records are nodes and scored
pairs are edges. Resolution is performed collectively with correlation
clustering over the graph, so a record's final cluster depends on its
neighbourhood rather than on a fixed pairwise threshold. In the internal
taxonomy this is a Graph-clustering-based design.

## Operational notes

- Batch size is controlled by the caller; the library keeps no global state.
- Scores are written to the output stream together with the rule/model version.
