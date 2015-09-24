#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
from Netflix import netflix_solve, rmse

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # rmse
    # ----

    def test_rmse1 (self) :
        i = [1, 1, 1]
        j = [1, 1, 1]
        k = rmse(i, j)
        self.assertEqual(0, k)

    def test_rmse2 (self) :
        i = [1, 2, 3]
        j = [1, 1, 1]
        k = rmse(i, j)
        self.assertEqual(1.29, k)

    def test_rmse3 (self) :
        i = [-15, -100, 1000]
        j = [1, 1, 1]
        k = rmse(i, j)
        self.assertEqual(579.79, k)

    def test_rmse4 (self) :
        i = [15, 1, -1]
        j = [15, 1, 1]
        k = rmse(i, j)
        self.assertEqual(1.15, k)

    def test_rmse5 (self) :
        i = [12, 14, 16]
        j = [13, 15, 17]
        k = rmse(i, j)
        self.assertEqual(1, k)
    # -------------
    # netflix_solve
    # -------------

    def test_solve (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120")
        w = StringIO()
        netflix_solve(r,w)
        self.assertEqual(w.getvalue(), "1:\n3.7\n3.5\n3.6\n3.8\n0.74")


if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out



% cat TestNetflix.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Netflix         18      0      6      0   100%
TestNetflix     33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
