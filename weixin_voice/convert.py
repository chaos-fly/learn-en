#!/usr/bin/env python
#-*- coding:utf8 -*-
import os

class CovertWeixin:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.tmp_arm = 'tmp/tmp.arm'   # 临时silk编码文件
        self.tmp_pcm = 'tmp/tmp.pcm'   # 临时解码的音频文件

    def prepare_silk(self):
        """ 去除文件头的第一个字节
        """
        with open(self.src) as fp, open(self.tmp_arm, 'w') as out:
            s = bytes(fp.read())
            out.write(s[1:])

    def covert_pcm(self):
        """ 解码文件成原始流
        """
        os.system('./decoder %s %s' % (self.tmp_arm, self.tmp_pcm))

    def covert_mp3(self):
        """ 编码
        """
        os.system('ffmpeg -f s16le -ar 24k -ac 1 -i %s %s' % (self.tmp_pcm, self.dst))

    def run(self):
        self.prepare_silk()
        self.covert_pcm()
        self.covert_mp3()
        

if __name__ == '__main__':
    # 从手机上拷贝的微信语音文件目录
    i = 0
    for root, dirs, files in os.walk('./favorite', topdown=False):
        for name in files:
            target = os.path.join(root, name)
            outfile = os.path.join('audios', str(i) + ".mp3")
            cv = CovertWeixin(target, outfile)
            cv.run()
            i += 1

