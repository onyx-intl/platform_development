#!/usr/bin/python2.4
#
#
# Copyright 2009, The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Abstract Android test suite."""


class AbstractTestSuite(object):
  """Represents a generic test suite definition.

  TODO: rename this as AbstractTestDef.
  """

  def __init__(self):
    self._name = None
    self._build_path = None
    self._build_dependencies = []
    self._is_continuous = False
    self._suite = None
    self._description = ''
    self._extra_build_args = ''

  def GetName(self):
    return self._name

  def SetName(self, name):
    self._name = name
    return self

  def GetBuildPath(self):
    """Returns the build path of this test, relative to source tree root."""
    return self._build_path

  def SetBuildPath(self, build_path):
    self._build_path = build_path
    return self

  def GetBuildDependencies(self, options):
    """Returns a list of dependent build paths."""
    return self._build_dependencies

  def SetBuildDependencies(self, build_dependencies):
    self._build_dependencies = build_dependencies
    return self

  def IsContinuous(self):
    """Returns true if test is part of the continuous test."""
    return self._is_continuous

  def SetContinuous(self, continuous):
    self._is_continuous = continuous
    return self._is_continuous

  def GetSuite(self):
    """Returns the name of test' suite, or None."""
    return self._suite

  def SetSuite(self, suite):
    self._suite = suite
    return self

  def GetDescription(self):
    """Returns a description if available, an empty string otherwise."""
    return self._description

  def SetDescription(self, desc):
    self._description = desc
    return self

  def GetExtraBuildArgs(self):
    """Returns the extra build args if available, an empty string otherwise."""
    return self._extra_build_args

  def SetExtraBuildArgs(self, build_args):
    self._extra_build_args = build_args
    return self

  def Run(self, options, adb):
    """Runs the test.

    Subclasses must implement this.
    Args:
      options: global command line options
      adb: asdb_interface to device under test
    """
    raise NotImplementedError
