import sys
import os
import pytest  # 导入pytest用于异常断言

# 将项目根目录加入Python模块搜索路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import dedupe, add  # 导入被测试的函数


# 测试dedupe去重函数
def test_dedupe_basic():
    assert dedupe([1, 2, 2, 3]) == [1, 2, 3], "正常去重场景失败"

def test_dedupe_empty():
    assert dedupe([]) == [], "空列表去重场景失败"

def test_dedupe_boolean():
    assert dedupe([True, False, True]) == [True, False], "布尔值去重场景失败"


# 测试add加法函数
def test_add_integer():
    assert add(2, 4) == 6, "整数求和失败"

def test_add_float():
    assert add(2.5, 3.5) == 6.0, "浮点数求和失败"

def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("2", 3), "非数字输入未抛异常，测试失败"