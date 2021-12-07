"""
测试文件夹
"""
from directory import Directory

def test_disk_usage(path):
    dir = Directory(path)
    print(dir.disk_usage())

if __name__ == "__main__":
    test_disk_usage("D:\\BaiduNetdiskWorkspace\\文档")
