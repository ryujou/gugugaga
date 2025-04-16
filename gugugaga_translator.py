class GugugagaTranslator: # 该类用于将文本转换为自定义编码方案“Gugugaga”或从中解码。
    """
    Gugugaga Translator类，用于使用自定义方案对文本进行编码和解码。
    """
    __GuguGaga = "灵感咕嘎" # 默认编码方案

    def __init__(self, newGuguGaga=None): # 构造函数，用于初始化编码方案。
        """ 
        初始化GugugagaTranslator，支持自定义编码方案。
        :param newGuguGaga: 一个包含4个字符的字符串，用作编码方案。
        """
        self.setGuguGaga(newGuguGaga)

    def convert(self, txt=""): # 将给定文本转换为自定义编码方案。
        """
        将给定文本转换为Gugugaga编码方案。
        :param txt: 要转换的文本。
        :return: 转换后的Gugugaga编码文本。
        """
        txt = txt.strip()
        if len(txt) < 1:
            return ""
        result = self.__GuguGaga[3] + self.__GuguGaga[1] + self.__GuguGaga[0]
        offset = 0
        for t in txt:
            c = ord(t)
            b = 12
            while b >= 0:
                hex = (c >> b) + offset & 15
                offset += 1
                result += self.__GuguGaga[int(hex >> 2)]
                result += self.__GuguGaga[int(hex & 3)]
                b -= 4
        result += self.__GuguGaga[2]
        return result

    def deConvert(self, txt): # 将自定义编码文本解码为原始文本。
        """
        将Gugugaga编码文本解码为原始文本。
        :param txt: 要解码的文本。
        :return: 解码后的原始文本。
        """
        txt = txt.strip()
        if not self.identify(txt):
            return "格式不正确！"
        result = ""
        i = 3
        offset = 0
        while i < len(txt) - 1:
            c = 0
            b = i + 8
            while i < b:
                n1 = self.__GuguGaga.index(txt[i])
                i += 1
                n2 = self.__GuguGaga.index(txt[i])
                c = c << 4 | ((n1 << 2 | n2) + offset) & 15
                if offset == 0:
                    offset = 0x10000 * 0x10000 - 1
                else:
                    offset -= 1
                i += 1
            result += chr(c)
        return result

    def identify(self, txt): # 检查给定文本是否符合自定义编码方案的格式。
        """
        检查给定文本是否符合Gugugaga编码格式。
        :param txt: 要检查的文本。
        :return: 如果符合格式返回True，否则返回False。
        """
        if txt:
            txt = txt.strip()
            if len(txt) > 11:
                if (
                    txt[0] == self.__GuguGaga[3]
                    and txt[1] == self.__GuguGaga[1]
                    and txt[2] == self.__GuguGaga[0]
                    and txt[-1] == self.__GuguGaga[2]
                    and ((len(txt) - 4) % 8) == 0
                ):
                    for t in txt:
                        if t not in self.__GuguGaga:
                            return False
                    return True
        return False

    def setGuguGaga(self, guguTxt): # 设置新的编码方案。
        """
        设置新的Gugugaga编码方案。
        :param guguTxt: 一个包含4个字符的字符串，用作新的编码方案。
        :return: 如果新编码方案有效返回True，否则返回False。
        """
        if guguTxt:
            guguTxt = guguTxt.strip()
            if len(guguTxt) == 4:
                self.__GuguGaga = guguTxt
                return True
        return False

    def getGuguGaga(self): # 返回当前的编码方案。
        """
        获取当前的编码方案。
        :return: 当前的编码方案。
        """
        return self.__GuguGaga
