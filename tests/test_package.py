"""import tests."""

import os
import importlib

import pytest

import service
import gui
import eos
import utils


def test_packages():
    assert service
    assert gui
    assert eos
    assert utils


def service_modules():
    for root, folders, files in os.walk("service"):
        for file_ in files:
            if file_.endswith(".py") and not file_.startswith("_"):
                mod_name = "{}.{}".format(
                    root.replace("/", "."),
                    file_.split(".py")[0],
                )
                yield mod_name


def eos_modules():
    for root, folders, files in os.walk("eos"):
        for file_ in files:
            if file_.endswith(".py") and not file_.startswith("_"):
                mod_name = "{}.{}".format(
                    root.replace("/", "."),
                    file_.split(".py")[0],
                )
                yield mod_name

# Disable test
'''
@pytest.mark.parametrize("mod_name", eos_modules())
def test_eos_imports(mod_name):
    assert importlib.import_module(mod_name)
'''
