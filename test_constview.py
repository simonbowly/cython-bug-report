import pyximport

pyximport.install()

import array
import numpy as np
import constview_cy


def test_numpy():
    arg = np.require(["a", "b"], dtype="S1", requirements=["C"])
    constview_cy.func(arg)


def test_array():
    arg = array.array("b", [1, 2])
    constview_cy.func(arg)
