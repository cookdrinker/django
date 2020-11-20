#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/11/20 18:06
# @Author: Tim Lin
# @FileName: test_make_toast.py.py

from django.shortcuts import make_toast
from django.test import SimpleTestCase

class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(make_toast(), 'toast')
