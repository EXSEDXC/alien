import sys
import os

def get_embedded_image(image_filename):
    """获取图片的正确路径，适配开发/打包状态"""
    if getattr(sys, "frozen", False):
        # 打包后：从PyInstaller临时目录加载
        base_path = sys._MEIPASS
    else:
        # 开发时：从当前脚本所在目录的images文件夹加载
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "images", image_filename)