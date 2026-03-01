#!/bin/bash
set -e

# Default to running mode=full if nothing is specified
if [ -n "$SCENARIO" ]; then
    echo "Triggering test scenario: $SCENARIO via GitHub Actions..."
    python run_tests.py --scenario "$SCENARIO"
elif [ -n "$MODE" ]; then
    echo "Triggering test mode: $MODE via GitHub Actions..."
    python run_tests.py --mode "$MODE"
else
    echo "No scenario or mode provided. Falling back to default full execution."
    python run_tests.py --mode full
fi
