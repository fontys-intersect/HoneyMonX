# Copyright (C) 2018 Billy Ferguson <wferguson@blueprintpower.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import random


class Random8BitRegisters:
    def __init__(self):
        self.key_num = random.SystemRandom()

    def get_value(self):
        values = [self.key_num.randint(0, 1) for b in range(0, 8)]
        return values


class Random16bitRegister:
    def __init__(self):
        self.key_num = random.SystemRandom()

    def get_value(self):
        return [self.key_num.randint(0, 1)]


# self defined ranges
class RandomValueBetween2And35:
    def __init__(self, previous=-1):
        if previous >= 0:
            initial = previous
        else:
            initial = 33
        self.previous = initial

        self.start = 2
        self.end = 35

    def get_value(self):
        self.case = random.randint(0, 50)
        if self.case < 25 and self.previous > self.start:
            self.previous -= 1
        else:
            if self.previous < self.end:
                self.previous += 1
        return self.previous


class RandomValueBetween20And50:
    def __init__(self, previous=-1):
        if previous >= 0:
            initial = previous
        else:
            initial = 25
        self.previous = initial

        self.start = 20
        self.end = 50

    def get_value(self):
        self.case = random.randint(0, 50)
        if self.case < 25 and self.previous > self.start:
            self.previous -= 1
        else:
            if self.previous < self.end:
                self.previous += 1
        return self.previous
