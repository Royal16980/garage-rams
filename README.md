# garage-rams

Risk Assessment App

This project implements a simple risk assessment tool with:

- Core assessment logic that computes a qualitative risk level.
- A small command line interface to run assessments.
- Automated tests verifying the behavior.

## Usage

Run the command line interface by providing probability and impact values between 0 and 1:

```bash
python -m garage_rams.ui --probability 0.5 --impact 0.8
```

## Development

Install dependencies and run the test suite with:

```bash
pip install -r requirements.txt  # if using a virtual environment
pytest
```
