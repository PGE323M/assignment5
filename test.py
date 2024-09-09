#!/usr/bin/env python

# Copyright 2018-2020 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert

with open("assignment5.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment5.py", "w") as f:
    f.write(python_file)

from assignment5 import *

class TestSolution(unittest.TestCase):

    def test_field_to_si(self):
        conv = FieldtoSI()
        assert abs(conv.viscosity(10) - 0.01) <= 1e-6
        assert abs(conv.pressure(1) - 6894.76) <= 1e-6
        assert abs(conv.permeability(1) - 9.869233e-16) <= 1e-6
        assert abs(conv.volume(1) - 0.0283168) <= 1e-6
        assert abs(conv.volume_rate(10000) - 0.0032774128000000002) <= 1e-6
        assert abs(conv.time(1) - 86400) <= 1e-6
        assert abs(conv.density(1) - 0.0160185) <= 1e-6
        assert abs(conv.compressibility(1) - 0.0001450376807894691) <= 1e-6
        assert abs(conv.temperature(72) - 22.22222222222222) <= 1e-6

    def test_si_to_field(self):
        conv = SItoField()
        assert abs(conv.viscosity(0.01) - 10) <= 1e-6
        assert abs(conv.pressure(6894.76) - 1) <= 1e-6
        assert abs(conv.permeability(9.869233e-16) - 1) <= 1e-6
        assert abs(conv.volume(0.028316846592000004) - 1) <= 1e-6
        assert abs(conv.volume_rate(0.0032774128000000002) - 10000) <= 1e-6
        assert abs(conv.time(86400) - 1) <= 1e-6
        assert abs(conv.density(0.0160185) - 1) <= 1e-6
        assert abs(conv.compressibility(0.0001450376807894691) - 1) <= 1e-6
        assert abs(conv.temperature(22.22222222222222) - 72) <= 1e-6

if __name__ == '__main__':
    unittest.main()
