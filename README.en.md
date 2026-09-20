# Korean Math Reinforcement Learning Environment

[🇰🇷 한국어](README.md) | [🇺🇸 English](README.en.md)

An experimental environment for training Korean mathematical-reasoning models with reinforcement learning.

## Goals

- Improve mathematical reasoning over a base model.
- Apply reinforcement-learning methods such as GRPO.
- Provide Korean-focused environment, tool-use, data loading, and verification components.

## Layout

- `src/math_rl/`: environment, data loader, tools, and verifiers
- `data/sample.jsonl`: sample data
- `tests/`: unit tests for the environment and tools

## Quick start

```bash
pip install -e .
pytest -q
python main.py
```

> A suitable GPU environment and model configuration are required for meaningful training runs.
