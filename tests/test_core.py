import os
import subprocess
import sys

import pytest

# Ensure package root is on the path when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from garage_rams.core import risk_level


def test_risk_level_low():
    assert risk_level(0.2, 0.5) == "low"

def test_risk_level_medium():
    assert risk_level(0.5, 0.8) == "medium"

def test_risk_level_high():
    assert risk_level(0.9, 0.9) == "high"

def test_invalid_values_raise():
    with pytest.raises(ValueError):
        risk_level(1.2, 0.5)


def test_cli_output():
    result = subprocess.run(
        [sys.executable, "-m", "garage_rams.ui", "--probability", "0.5", "--impact", "0.8"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Risk level: medium" in result.stdout
