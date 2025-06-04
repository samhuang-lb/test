import os
import threading
import asyncio
import time
from functools import wraps
from dataclasses import dataclass
from typing import  Optional, Union

# 装饰器：函数计时
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行耗时: {end_time - start_time:.4f}秒")
        return result
    return wrapper

# 数据类：表示书籍
@dataclass
class Book:
    title: str
    author: str
    year: int
    pages: int
    isbn: str
    
    def get_info(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

# 异步函数：模拟网络请求
async def fetch_data(url: str) -> str:
    print(f"开始请求: {url}")
    await asyncio.sleep(1)  # 模拟网络延迟
    return f"数据来自 {url}"

# 多线程类：文件处理
class FileProcessor(threading.Thread):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path
        
    def run(self) -> None:
        try:
            size = os.path.getsize(self.file_path)
            print(f"文件 {self.file_path} 大小: {size} 字节")
        except Exception as e:
            print(f"处理文件时出错: {e}")

# 生成器函数：斐波那契数列
def fibonacci_generator(max_num: int) -> Union[int, None]:
    a, b = 0, 1
    while a < max_num:
        yield a
        a, b = b, a + b

# 元类：单例模式
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# 使用单例元类的类
class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {
            "debug": True,
            "host": "localhost",
            "port": 8080
        }
    
    def get_setting(self, key: str) -> Optional[Union[str, int, bool]]:
        return self.settings.get(key)

# 主函数
@timer_decorator
def main() -> None:
    template="牛逼 {first} {second}"
    prompt=template.format(first="sam",second="huang")
    print(prompt)
    # 创建书籍对象
    book1 = Book("Python Cookbook", "David Beazley", 2013, 700, "978-1449340377")
    print(f"书籍信息: {book1.get_info()}")
    
    # 异步任务
    async def run_async_tasks():
        tasks = [fetch_data(f"https://api.example.com/data/{i}") for i in range(3)]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)
    
    asyncio.run(run_async_tasks())
    
    # 多线程处理
    files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in files:
        processor = FileProcessor(file)
        processor.start()
    
    # 斐波那契生成器
    fib_nums = list(fibonacci_generator(100))
    print(f"斐波那契数列: {fib_nums}")
    
    # 单例模式
    config1 = AppConfig()
    config2 = AppConfig()
    print(f"config1 和 config2 是同一个实例: {config1 is config2}")

if __name__ == "__main__":
    main()    