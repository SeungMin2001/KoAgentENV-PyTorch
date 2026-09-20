# 한국어 수학 강화학습 환경

[🇰🇷 한국어](README.md) | [🇺🇸 English](README.en.md)

강화학습을 통해 한국어 수학 추론 모델을 만들기 위한 실험 환경입니다.

## 목표

- 기존 모델의 수학 추론 능력 개선
- GRPO 등 강화학습 기법 적용
- 학습·검증·도구 호출을 위한 한국어 환경 제공

## 구성

- `src/math_rl/`: 환경, 데이터 로더, 도구, 검증 로직
- `data/sample.jsonl`: 예시 데이터
- `tests/`: 환경과 도구의 단위 테스트

## 시작하기

```bash
pip install -e .
pytest -q
python main.py
```

> GPU 환경과 모델 설정은 실험 규모에 맞춰 별도로 준비해야 합니다.

