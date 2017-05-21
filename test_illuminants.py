'''
test_illuminants.py - Test module for illuminants.py.

License:

Copyright (C) 2008 Mark Kness

Author - Mark Kness - mkness@alumni.utexas.net

This file is part of ColorPy.

ColorPy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

ColorPy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with ColorPy.  If not, see <http://www.gnu.org/licenses/>.
'''


from . import illuminants

def test (verbose=0):
    '''Mainly call some functions.'''
    D65 = illuminants.get_illuminant_D65()
    if verbose >= 1:
        print('Illuminant D65')
        print(str (D65))
    A = illuminants.get_illuminant_A()
    if verbose >= 1:
        print('Illuminant A')
        print(str (A))
    const = illuminants.get_constant_illuminant()
    if verbose >= 1:
        print('Constant Illuminant')
        print(str (const))

    T_list = [0.0, 1.0, 100.0, 1000.0, 5778.0, 10000.0, 100000.0]
    for T in T_list:
        bb = illuminants.get_blackbody_illuminant (T)
        if verbose >= 1:
            print('Blackbody Illuminant : %g K' % (T))
            print(str (bb))
    print('test_illuminants.test() passed.')
   
