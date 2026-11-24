# makefun-chess

A chess engine in 4 KB of Python for the [make.fun](https://make.fun) **tiny-chess-01** bounty.

## Features

- Alpha-beta search with iterative deepening (up to depth 8)
- 10x12 mailbox board with rotation trick for color flipping
- Check extensions, futility pruning, killer move heuristic
- MVV capture ordering, quiescence search with promotions
- Transposition table for best-move ordering
- Fully deterministic (fixed node budget, no clock)

## Constraints

- `main.py` must be <= 4,096 bytes
- Python 3.13 stdlib only
- 10-second per-move time limit
- Deterministic replay required

## Run locally

```bash
node tiny-chess-01-kit/cli/makefun.mjs grade-local --kit tiny-chess-01-kit --bot . --driver process
```
