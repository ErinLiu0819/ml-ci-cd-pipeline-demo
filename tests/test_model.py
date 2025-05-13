import pytest 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 测试模型训练是否正常
def test_model_training():
    # 加载数据并拆分
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
    
    # 训练模型
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # 断言：模型在测试集上的准确率应大于90%
    assert model.score(X_test, y_test) > 0.9