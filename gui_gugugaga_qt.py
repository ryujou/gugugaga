import sys 
import os
import multiprocessing
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton, QLabel,
    QFileDialog, QVBoxLayout, QWidget, QMessageBox
)
from PyQt5.QtGui import QIcon
from file_gugugaga_encoder import FileGugugagaEncoder

def resource_path(relative_path):
    # 获取资源文件的路径，兼容打包后的环境
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class GugugagaMainWindow(QMainWindow):
    def __init__(self):
        # 初始化主窗口
        super().__init__()
        self.setWindowTitle("🍄灵感咕嘎加密器🍄")
        self.setWindowIcon(QIcon(resource_path("icon.ico")))
        self.encoder = FileGugugagaEncoder()

        # 创建文本输入和输出框
        self.text_input = QTextEdit()
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        # 创建标签
        self.label = QLabel("支持文本加解密和文件加解密")

        # 创建按钮
        btn_encrypt = QPushButton("加密文本")
        btn_decrypt = QPushButton("解密文本")
        btn_file_open = QPushButton("选择文件加密")
        btn_file_decode = QPushButton("选择文件解密")

        # 绑定按钮事件
        btn_encrypt.clicked.connect(self.encrypt_text)
        btn_decrypt.clicked.connect(self.decrypt_text)
        btn_file_open.clicked.connect(self.select_file_encrypt)
        btn_file_decode.clicked.connect(self.select_file_decrypt)

        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(btn_encrypt)
        layout.addWidget(btn_decrypt)
        layout.addWidget(btn_file_open)
        layout.addWidget(btn_file_decode)
        layout.addWidget(self.text_output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encrypt_text(self):
        # 加密文本输入框中的内容
        plain = self.text_input.toPlainText().strip()
        self.text_output.clear()
        if not plain:
            QMessageBox.warning(self, "提示", "请输入文本")
            return
        encrypted = ''.join(self.encoder.translator.convert(c) for c in plain)
        self.text_output.setPlainText(encrypted)

    def decrypt_text(self):
        # 解密文本输入框中的内容
        text = self.text_input.toPlainText().strip()
        self.text_output.clear()
        if not text:
            QMessageBox.warning(self, "提示", "请输入加密文本")
            return
        unit_len = len(self.encoder.translator.convert("A"))
        try:
            chunks = [text[i:i + unit_len] for i in range(0, len(text), unit_len)]
            decrypted = ''.join(self.encoder.translator.deConvert(c) for c in chunks)
            self.text_output.setPlainText(decrypted)
        except Exception as e:
            self.text_output.setPlainText("[错误] 解密失败：" + str(e))

    def select_file_encrypt(self):
        # 选择文件并对其进行加密
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件加密")
        if not file_path:
            return
        self.text_output.clear()
        try:
            encrypted = self.encoder.encode_file_to_gugugaga(file_path)
            dir_path = os.path.dirname(file_path)
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            save_path = os.path.join(dir_path, f"encode_{base_name}.txt")

            with open(save_path, "w", encoding="utf-8") as f:
                f.write(encrypted)

            self.text_output.setPlainText(encrypted)
            QMessageBox.information(self, "成功", f"加密完成，保存路径：\n{save_path}")
            os.startfile(dir_path)

        except Exception as e:
            QMessageBox.critical(self, "错误", f"加密失败：{e}")

    def select_file_decrypt(self):
        # 选择加密文件并对其进行解密
        input_path, _ = QFileDialog.getOpenFileName(self, "选择加密文件")
        if not input_path:
            return
        self.text_output.clear()
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                encoded = f.read()
            base = os.path.splitext(input_path)[0]
            output_path = self.encoder.decode_gugugaga_to_file(encoded, base + "_decoded")
            QMessageBox.information(self, "完成", f"解密完成，已保存为：\n{output_path}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"解密失败：{e}")

def main():
    # 程序入口，初始化应用程序
    multiprocessing.freeze_support()  # Windows 兼容
    app = QApplication(sys.argv)
    win = GugugagaMainWindow()
    win.resize(800, 600)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
