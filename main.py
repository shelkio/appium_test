import os
import pytest

pytest.main(["-q", "--alluredir=./report/tmp","--clean-alluredir"])
os.system("allure generate -c -o ./report/html ./report/tmp")
# os.system("allure open ./report/html")


# -s：显示程序中的 print/logging 输出。
# -v：丰富信息模式, 输出更详细的用例执行信息。
# -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
# -q：简单输出模式, 不输出环境信息。
# -x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
