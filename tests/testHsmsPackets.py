#####################################################################
# testHsmsPacket.py
#
# (c) Copyright 2013-2016, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################

import secsgem

import unittest

class TestHsmsPacket(unittest.TestCase):
    def testConstructorWithoutHeader(self):
        packet = secsgem.HsmsPacket()

        self.assertEqual(packet.header.stream, 0)
        self.assertEqual(packet.header.function, 0)