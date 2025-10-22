import sys
import os
import pytest  # 导入pytest用于异常断言（保留必要依赖）

# 获取仓库根目录路径（当前测试文件的“上上级”目录，仅需配置一次）
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)  # 将根目录加入模块搜索路径（仅需添加一次）

from app.app import dedupe, add  # 导入被测试的函数（仅需导入一次）


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
        add("2", 3)  # 注意：原代码中多余的逗号已移除，避免语法警告
    # 断言信息可直接写在with语句后或函数注释中，此处简化逻辑