
# train_nlu.py ：train NLU model

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer


# 训练模型
def train():
    # 示例数据
    training_data = load_data('data/train_data.json')
    # pipeline配置
    trainer = Trainer(config.load("nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(
        './projects/default/')  # 返回nlu模型的储存位置；如果config文件中没有project_name，模型会存储在默认的 /models/default 文件夹下


# 识别意图
def predict(model_directory):
    from rasa_nlu.model import Metadata, Interpreter
    # 用nlu模型初始化interpreter； `model_directory`为nlu模型位置
    interpreter = Interpreter.load(model_directory, config.load("sample_configs/config_jieba_mitie_sklearn.json"))
    # 使用加载的interpreter处理文本
    print(interpreter.parse(u"我想吃麻辣烫"))


if __name__ == '__main__':
    train()
