"""Core risk assessment logic."""

def risk_level(probability: float, impact: float) -> str:
    """Calculate qualitative risk level.

    Risk score is probability * impact.
    Returns 'low', 'medium', or 'high' based on thresholds.
    """
    if not 0 <= probability <= 1 or not 0 <= impact <= 1:
        raise ValueError("probability and impact must be between 0 and 1")

    score = probability * impact
    if score < 0.3:
        return "low"
    if score < 0.7:
        return "medium"
    return "high"
