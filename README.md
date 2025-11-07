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

## Deployment

Package the project into a wheel or source archive so it can be installed on
other machines or uploaded to a package index:

```bash
python -m pip install --upgrade build
python -m build
```

The build command creates artifacts in the `dist/` directory. Install the
package locally to verify the console script entry point:

```bash
python -m pip install dist/garage_rams-0.1.0-py3-none-any.whl
garage-rams --probability 0.4 --impact 0.9
```

To distribute the project, upload the contents of `dist/` to your preferred
package index (for example, [PyPI](https://pypi.org/)) or copy the wheel to the
target environment and install it there.
