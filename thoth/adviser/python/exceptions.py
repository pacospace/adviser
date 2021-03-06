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

"""Exceptions related to Python recommendations."""

from ..exceptions import ThothAdviserException


class DirectDependencyRemoval(ThothAdviserException):
    """Raised if trying to remove direct dependency from application stack.

    Or there is no option to remove the given dependency from application stack.
    """


class UnableLock(ThothAdviserException):
    """Raised if trying to lock invalid application stack or resolution cannot be done."""


class ConstraintClashError(ThothAdviserException):
    """An exception raised if there is a clash with constraints (see dependency graph for more info)."""
