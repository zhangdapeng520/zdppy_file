"""
文件夹相关
"""
import os

class Directory:
    def __init__(self, path:str) -> None:
        """
        path: 文件夹路径
        """
        self.path = path
    
    def disk_usage(self):
        """
        查看文件夹的占用量
        """
        # 使用内部函数避开递归函数self问题
        def inner_disk_usage(path):
            total = os.path.getsize(path)
            if os.path.isdir(path):  # 如果是文件夹
                for file_name in os.listdir(path):
                    child_path = os.path.join(path, file_name)
                    total += inner_disk_usage(child_path)
            
            # 打印当前目录的占用大小
            print("{0:<7}".format(total), path)
            return total
        
        # 调用内部递归函数
        return inner_disk_usage(self.path)