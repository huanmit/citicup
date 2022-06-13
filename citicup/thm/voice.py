from cmath import cos
from bert_serving.client import BertClient
import speech_recognition as sr
import numpy as np

# Working with audio files
r = sr.Recognizer()
# bc = BertClient(ip='10.60.38.173',check_length=False)# ip中是部署了bert模型的服务器地址

stc = [
    "过去一个月我在碳币排行榜上排多少名",
    "我现在有多少碳币",
    "我的碳信用分数是多少",
]
vec = []
#vec = bc.encode(stc)
#np.save('./bert_vec.npy',vec)
input_vec = np.load('./input.npy')
vec = np.load('./bert_vec.npy')



print("您可以向我查询碳币、碳信用等等..."+'\n'+'请说话：')
microphone = sr.Microphone()
with microphone as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    # sentence = r.recognize_sphinx(audio)
    input_sentence = r.recognize_google(audio,language="cmn-Hans-CN") #简体中文
    # 计算用户说的句子的bert向量
    input_vec = bc.encode([input_sentence])
    print(input_sentence)
except:
    print("无法识别出句子，请重试。")

# 将输入句子的向量与预设句子的向量一一求出余弦值，与余弦值最大的匹配成功
cos_input = []
for each in vec:
    each = each.reshape(768,1)
    res = input_vec.dot(each) / (np.linalg.norm(input_vec) * np.linalg.norm(each))
    res = (res[0][0])
    cos_input.append(res)
print(cos_input)
index = cos_input.index(max(cos_input))
print('检测到输入应为预设库中的第'+str(index+1)+'条，“',stc[index]+'”')
#cos_input = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
