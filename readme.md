# Alien Invasion（外星人入侵游戏）
图片素材来源网络
## 功能说明
按照《Python编程：从入门到实践（第3版）》完成的一个基于 Pygame 的经典射击游戏，支持单文件 EXE 打包。

## 运行方法
1. 安装依赖：
   pip install pygame pyinstaller
2. 本地运行：
    python alien_invasion.py
3. 打包成单文件 EXE：
    pyinstaller --onefile --windowed --add-data "images/*;images" --exclude-module pygame.tests --strip alien_invasion.py
4. 注意images中的图片资源