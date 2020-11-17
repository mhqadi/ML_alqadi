#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ml_alqadi` package."""

# Third party modules
import pytest

# First party modules
import ml_alqadi


def test_version():
    assert ml_alqadi.__version__.count(".") == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
