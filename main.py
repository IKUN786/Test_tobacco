import os
import sys
import pytest
from pathlib import Path

# -------------------------- 1. 路径安全处理 --------------------------
# 获取项目根目录（main.py 所在的目录）
BASE_DIR = Path(__file__).resolve().parent
# 将项目根目录加入 sys.path，彻底解决模块导入报错
sys.path.insert(0, str(BASE_DIR))

# -------------------------- 2. 目录定义 --------------------------
# Allure 临时结果目录（pytest 生成的原始数据）
ALLURE_RESULTS_DIR = BASE_DIR / "report" / "allure-results"
# Allure 最终 HTML 报告目录
ALLURE_REPORT_DIR = BASE_DIR / "report" / "allure-report"

# -------------------------- 3. 运行测试 --------------------------
def run():
    print("=" * 50)
    print("🚀 开始执行接口自动化测试...")
    print("=" * 50)

    # 3.1 运行 pytest 并生成 Allure 原始结果
    # 参数说明：
    # testcases/ : 指定测试用例目录
    # -v : 显示详细用例执行信息
    # -s : 允许 print 输出到控制台
    # --alluredir : 指定 Allure 结果存放路径
    # --clean-alluredir : 运行前清空旧结果
    pytest.main([
        "testcases/",
        "-v",
        "-s",
        f"--alluredir={ALLURE_RESULTS_DIR}",
        "--clean-alluredir"
    ])

    # -------------------------- 4. 生成 Allure 报告 --------------------------
    print("\n" + "=" * 50)
    print("📊 正在生成 Allure 测试报告...")
    print("=" * 50)

    # 生成报告命令：
    # allure generate <结果目录> -o <报告目录> -c
    # -c : 清空报告目录旧数据
    os.system(f"allure generate {ALLURE_RESULTS_DIR} -o {ALLURE_REPORT_DIR} -c")

    # -------------------------- 5. 自动打开报告（可选） --------------------------
    print("\n✅ 测试执行完毕！正在打开报告...")
    os.system(f"allure open {ALLURE_REPORT_DIR}")

if __name__ == "__main__":
    run()