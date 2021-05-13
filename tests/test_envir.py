#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `envir` package."""

import pytest
import os

import envir


def test_str():

    os.environ['ENVIR_TEST_VARIABLE'] = '123'

    assert '123' == envir.load('ENVIR_TEST_VARIABLE')

    assert '123' == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.STR)

    os.environ.pop('ENVIR_TEST_VARIABLE')


def test_int():

    os.environ['ENVIR_TEST_VARIABLE'] = '123'

    assert 123 == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.INT)

    os.environ.pop('ENVIR_TEST_VARIABLE')


def test_float():

    os.environ['ENVIR_TEST_VARIABLE'] = '123.1'

    assert 123.1 == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.FLOAT)

    os.environ.pop('ENVIR_TEST_VARIABLE')


def test_bool():

    os.environ['ENVIR_TEST_VARIABLE'] = 'true'

    assert True == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.BOOL)

    os.environ.pop('ENVIR_TEST_VARIABLE')


def test_default():

    assert '123' == envir.load('ENVIR_TEST_VARIABLE', default='123')
    assert '123' == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.STR, default='123')
    assert 123 == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.INT, default=123)
    assert 123.1 == envir.load('ENVIR_TEST_VARIABLE', formatter=envir.FLOAT, default=123.1)
    assert True is envir.load('ENVIR_TEST_VARIABLE', formatter=envir.BOOL, default=True)
    assert False is envir.load('ENVIR_TEST_VARIABLE', formatter=envir.BOOL, default=False)
