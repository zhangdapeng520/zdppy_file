# zdpapi_file
Python操作文件和文件夹的便捷组件库

项目地址：https://github.com/zhangdapeng520/zdpapi_file

## 一、概述

### 1.1 功能

- 查看文件夹占用磁盘大小


## 二、快速入门

### 2.1 查看文件夹占用磁盘大小
```python
from zdpapi_file import Directory

def test_disk_usage(path):
    dir = Directory(path)
    print(dir.disk_usage())

if __name__ == "__main__":
    test_disk_usage("D:\\BaiduNetdiskWorkspace\\文档")
```
