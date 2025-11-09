"""Minimal epistemic state helper for LLM agents."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Tuple


@dataclass
class Announcement:
    """Structured fact stored in the knowledge base."""

    proposition: str
    source: str
    confidence: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            msg = f"confidence must be in [0, 1], got {self.confidence}"
            raise ValueError(msg)


@dataclass
class KnowledgeBase:
    """Tracks announcements and basic entailment checks."""

    facts: Dict[str, Announcement] = field(default_factory=dict)
    inconsistencies: List[Tuple[str, Announcement, Announcement]] = field(default_factory=list)

    def update(self, announcement: Announcement) -> None:
        """Add or revise a fact, logging inconsistencies for review."""

        existing = self.facts.get(announcement.proposition)
        if existing and existing.proposition.startswith("not ") != announcement.proposition.startswith("not "):
            self.inconsistencies.append((announcement.proposition, existing, announcement))
        self.facts[announcement.proposition] = announcement

    def entails(self, proposition: str) -> bool:
        """Return True if the proposition or its synonyms are present."""

        if proposition in self.facts:
            return True
        negative = f"not {proposition}"
        if negative in self.facts:
            return False
        return False

    def export_prompt(self) -> str:
        """Render the knowledge base as a bullet list for prompt injection."""

        lines: Iterable[str] = (
            f"- {fact.proposition} (source={fact.source}, p={fact.confidence:.2f})"
            for fact in self.facts.values()
        )
        return "\n".join(lines)
