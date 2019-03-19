python -m rasa_nlu.train -c sample_configs/config_jieba_mitie_sklearn.yml --data data/examples/rasa/demo-rasa_zh.json --path models




pip install rasa_core
pip install rasa_nlu[tensorflow]
#自动管理版本
pip install pipenv


#模型训练
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue


#中文训练
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
#开启服务并测试
python -m rasa_core.run -d models/dialogue -u models/current/nlu

#1列出所有包的版本
pip freeze > requirements.txt
#2利用pipreqs
pip install pipreqs