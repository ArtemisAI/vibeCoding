"""A very small sanity test.

This keeps the CI green and guarantees that the test harness is wired
correctly.  Replace or extend it as soon as you add real functionality.
"""


def test_readme_exists():
    import pathlib

    readme = pathlib.Path(__file__).resolve().parents[1] / "README.md"
    assert readme.exists(), "README.md should exist at repository root"


def test_human_md_exists():
    import pathlib

    human = pathlib.Path(__file__).resolve().parents[1] / "HUMAN.md"
    assert human.exists(), "HUMAN.md should exist at repository root"
