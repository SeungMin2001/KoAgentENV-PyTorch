from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KOTRAJ_ROOT = PROJECT_ROOT / "third_party" / "kotraj-bench"

sys.path.insert(0, str(KOTRAJ_ROOT))

from tools.mock import make_env


def main():
    env = make_env(domain="calendar", seed=0)

    result = env.call(
        "list_events",
        {"date": "2026-08-04"},
    )

    assert result["ok"] is True
    assert result["today"] == "2026-08-03"
    assert len(result["events"]) == 1
    assert result["events"][0]["title"] == "팀 주간회의"

    assert env.exec_log == [
        {
            "name": "list_events",
            "args": {"date": "2026-08-04"},
            "ok": True,
        }
    ]

    print("KoTraj calendar smoke check passed.")


if __name__ == "__main__":
    main()