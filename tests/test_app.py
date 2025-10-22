# tests/test_app.py：针对dedupe和add函数的测试用例（依赖pytest）
import pytest
from app.app import dedupe, add

# 测试dedupe去重函数（覆盖正常场景、空列表、重复布尔值）
def test_dedupe_basic():
    assert dedupe([1, 2, 2, 3]) == [1, 2, 3], "正常去重场景失败"

def test_dedupe_empty():
    assert dedupe([]) == [], "空列表去重场景失败"

def test_dedupe_boolean():
    assert dedupe([True, False, True]) == [True, False], "布尔值去重场景失败"

# 测试add加法函数（覆盖整数、浮点数、异常场景）
def test_add_integer():
    assert add(2, 4) == 6, "整数求和失败"

def test_add_float():
    assert add(2.5, 3.5) == 6.0, "浮点数求和失败"

def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("2", 3), "非数字输入未抛异常，测试失败"