"""Toy agent loop showing how announcements update the knowledge base."""
from __future__ import annotations

from typing import Iterable

from knowledge_base import Announcement, KnowledgeBase


def diagnose(connectivity_checks: Iterable[str]) -> str:
    kb = KnowledgeBase()
    kb.update(Announcement("dns failure example.com", source="ping_test"))
    for check in connectivity_checks:
        if check.startswith("reachable "):
            kb.update(Announcement(check, source="user"))
    if kb.entails("dns failure example.com"):
        return "Recommend refreshing DNS configuration"
    return "Escalate to network engineer"


if __name__ == "__main__":
    recommendation = diagnose(["reachable via ip 93.184.216.34"])
    print(recommendation)
