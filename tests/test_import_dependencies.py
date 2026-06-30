import pytest

# List of dependencies
dependencies = [
    "rasters",
    "sentinel_tiles"
]

# Generate individual test functions for each dependency
@pytest.mark.parametrize("dependency", dependencies)
def test_dependency_import(dependency):
    __import__(dependency)
