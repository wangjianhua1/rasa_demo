python -m rasa_nlu.train -c sample_configs/config_jieba_mitie_sklearn.yml --data data/examples/rasa/demo-rasa_zh.json --path models

pip install rasa_core
pip install rasa_nlu[tensorflow]
#自动管理版本
pip install pipenv
#1列出所有包的版本
pip freeze > requirements.txt
#2利用pipreqs
pip install pipreqs
pipreqs ./ --encoding=utf-8

#插槽使用
https://terrifyzhao.github.io/2019/02/26/Rasa%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%9702.html

pip install rasa_core_sdk


#(1)模型训练
###(没有3之前)python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue -c policy_config.yml
#(2)中文训练
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
#(3)开启action
python -m rasa_core_sdk.endpoint --actions action
#(4)开启服务并测试
###(没有3之前) python -m rasa_core.run -d models/dialogue -u models/current/nlu
python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml


