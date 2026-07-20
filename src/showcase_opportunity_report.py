from dataclasses import dataclass


@dataclass(frozen=True)
class OpportunitySignals:
    market_demand: int
    competition: int
    keyword_opportunity: int
    content_quality_gap: int


def summarize_opportunity(signals: OpportunitySignals) -> dict[str, object]:
    score = round(
        signals.market_demand * 0.35
        + (100 - signals.competition) * 0.25
        + signals.keyword_opportunity * 0.25
        + signals.content_quality_gap * 0.15
    )

    if score >= 75:
        recommendation = "Strong opportunity worth deeper supplier validation."
    elif score >= 55:
        recommendation = "Promising opportunity; improve content and images before scaling."
    else:
        recommendation = "High-risk opportunity; validate demand and margins first."

    return {
        "score": score,
        "recommendation": recommendation,
        "signals": signals,
    }
