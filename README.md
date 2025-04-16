# 🍄灵感咕嘎加密器🍄

### 本项目99.99%使用GPT4.5辅助编写,包括此README

一个支持**文本和文件加密解密**的图形化应用，使用自定义字符表（默认 `"灵感咕嘎"`）将明文转化为咆哮风格的密文。  
支持 Base64 + 咕嘎映射算法，具备 **自动识别文件类型**、**自定义字符表**、**图形界面**、**多进程并行加速**等功能。

---

## 🖥 功能特点

- ✅ 文本加密/解密（咕嘎风格字符映射）
- ✅ 文件加密（自动转 Base64 + 字符映射）
- ✅ 文件解密（自动识别原始类型并恢复）
- ✅ 自动命名：如 `encode_文件名_.txt`，解密为 `原名_decoded.类型`
- ✅ 图形界面（使用 PyQt5）
- ✅ 多进程加速加密，提高大文件性能
- ✅ release可下载 `.exe` 可运行文件

---

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

> ⚠️ Windows 用户推荐使用虚拟环境（`python -m venv venv`）

---

## 🚀 启动程序

```bash
python gui_gugugaga_qt.py
```

---

## 🛠 打包为 .exe（可选）

使用 [PyInstaller](https://www.pyinstaller.org/) 将程序打包为独立 `.exe` 文件：

```bash
pyinstaller --noconsole --onefile --icon=icon.ico --add-data "icon.ico;." gui_gugugaga_qt.py
```

> 若需压缩可使用 `--upx-dir` 参数（需安装 [UPX](https://upx.github.io/)）

---

## 🧪 性能优化说明

- 使用 `multiprocessing.Pool` 实现 **多核并行字符加密**
- 加密速度较原始单线程提升 3~10 倍（视 CPU 而定）
- 避免字符串拼接瓶颈，使用 `''.join()` + 生成器方式

---

## 📂 项目结构

```
gugugaga_project/
├── gui_gugugaga_qt.py         # 主 GUI 界面入口
├── file_gugugaga_encoder.py   # 文件加密/解密与识别
├── gugugaga_translator.py     # 灵感咕嘎字符加解密核心
├── requirements.txt           # Python 依赖
├── icon.ico                   # 应用图标
```

---

## ✨ 灵感来源

灵感来自互联网流行的“兽音加密”与“咆哮体字符编码”。  
通过将任意明文字符映射为定制字符组合，实现高可读性密文格式。

---

## 📃 License

MIT License © 2024
