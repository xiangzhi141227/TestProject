import unittest

import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print('这是测试环境')
        if 'dev' in env:
            print('这是测试环境')
