# Orchestrated vHIL Framework for Surgical Robotics

## Overview
This is a Virtual Hardware-in-the-Loop (vHIL) framework for surgical robotics. It supports modular test suites for isolated and integrated checking. Components like CAN network signals and hardware sensors are mocked using Python's `unittest.mock`. 

## Project Structure
- `tests/unit/`: Logic checks for coordinate conversions.
- `tests/sensors/`: Simulated inputs for Force, Proximity, and Optical sensors.
- `tests/integration/`: End-to-end scenarios (Suture Simulation, Bone Drilling), designed to require a Virtual CAN interface.
- `run_tests.py`: Python wrapper Orchestrator.
- `pytest.ini`: Custom markers definition for easy filtering.

## Orchestrator Execution
Use `run_tests.py` to trigger specific testing segments.

### Options
- `--scenario <marker>`: Runs tests across the suite matching the given custom marker (e.g., `sensor`, `navigation`, `critical`).
- `--mode <directory/full>`: Runs all tests in a specified directory (e.g., `unit`, `sensors`, `integration`), or `full` for all available tests.

### Examples
- `python run_tests.py --scenario sensor`
- `python run_tests.py --mode integration`
- `python run_tests.py --mode full`

## Containerized the pipeline 
The test infrastructure can be run inside a Docker container, seamlessly accepting environment variables during execution, which makes it perfect for automation like GitHub Actions.

### Environment variables setup
- `SCENARIO`: Passes value to orchestrator's `--scenario`. E.g. `docker run -e SCENARIO=critical vhil-framework`
- `MODE`: Passes value to orchestrator's `--mode`. E.g. `docker run -e MODE=unit vhil-framework` 
- `VIRTUAL_CAN_ACTIVE`: Pass `1` to run integration tests (simulates an active virtual CAN system).

E.g. GitHub Actions Example for PR commits to trigger `critical` checks.
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: docker build -t vhil-framework .
      - run: docker run -e SCENARIO=critical vhil-framework
```
