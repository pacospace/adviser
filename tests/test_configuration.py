#!/usr/bin/env python3
# thoth-adviser
# Copyright(C) 2018, 2019 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Test adviser configuration setup."""

import os

from thoth.adviser.configuration import _Configuration
from thoth.python import Source

from base import AdviserTestCase


class TestConfiguration(AdviserTestCase):
    """Test adviser configuration setup."""

    def test_default(self):
        configuration = _Configuration()
        assert "THOTH_ADVISER_WAREHOUSES" not in os.environ
        assert configuration.warehouses is not None
        assert len(configuration.warehouses) == 2

        assert set(configuration.warehouses) == set(
            ("https://pypi.python.org/simple", "https://pypi.org/simple")
        )
