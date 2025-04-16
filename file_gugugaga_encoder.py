import base64
import magic
import multiprocessing
import os
from gugugaga_translator import GugugagaTranslator

MIME_EXTENSION_MAP = {
    "image/jpeg": "jpg",
    "image/png": "png",
    "image/gif": "gif",
    "application/pdf": "pdf",
    "application/zip": "zip",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
    "application/msword": "doc",
    "application/vnd.ms-excel": "xls",
    "text/plain": "txt",
    "text/html": "html",
    "application/json": "json",
    "application/x-rar-compressed": "rar",
    "application/x-executable": "exe",
    "application/octet-stream": "bin",
}

class FileGugugagaEncoder:
    def __init__(self, translator=None):
        # 初始化函数，设置翻译器和文件类型检测器
        self.translator = translator or GugugagaTranslator()
        self.magic_detector = magic.Magic(mime=True)

    def encode_file_to_gugugaga(self, input_path):
        # 将文件编码为Gugugaga格式
        # 1. 读取文件内容并转换为Base64字符串
        with open(input_path, "rb") as f:
            raw = f.read()

        base64_str = base64.b64encode(raw).decode("utf-8")

        # 2. 使用多进程加速字符转换
        with multiprocessing.Pool() as pool:
            encoded_list = pool.map(self.translator.convert, base64_str)

        # 3. 返回编码后的字符串
        return ''.join(encoded_list)

    def decode_gugugaga_to_file(self, encoded_str, output_base: str = "output"):
        # 将Gugugaga格式的字符串解码为文件
        # 1. 根据翻译器的单位长度分割编码字符串
        unit_len = len(self.translator.convert("A"))
        chunks = [encoded_str[i:i + unit_len] for i in range(0, len(encoded_str), unit_len)]
        
        # 2. 将分割后的字符串解码为Base64字符串
        base64_str = ''.join(self.translator.deConvert(chunk) for chunk in chunks)
        
        # 3. 解码Base64字符串为原始二进制数据
        raw = base64.b64decode(base64_str)

        # 4. 检测文件类型并生成文件扩展名
        ext = self.detect_file_type(raw)
        final_path = f"{output_base}.{ext}"

        # 5. 将二进制数据写入文件
        with open(final_path, "wb") as f:
            f.write(raw)

        # 6. 返回生成的文件路径
        return final_path

    def detect_file_type(self, data: bytes) -> str:
        # 检测文件类型并返回对应的扩展名
        # 1. 使用magic库检测文件的MIME类型
        mime_type = self.magic_detector.from_buffer(data)
        
        # 2. 根据MIME类型映射表返回扩展名，默认为"bin"
        return MIME_EXTENSION_MAP.get(mime_type, "bin")
