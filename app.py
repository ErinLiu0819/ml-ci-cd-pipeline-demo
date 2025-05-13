from fastapi import FastAPI
from pydantic import BaseModel  # 用于定义请求数据模型
import joblib
import numpy as np

# 加载训练好的模型
app = FastAPI()
model = joblib.load("model.joblib")

# 定义请求体格式（需包含4个特征值）
class RequestData(BaseModel):
    features: list[float]

# 创建API端点
@app.post("/predict")
def predict(data: RequestData):
    # 将输入特征转换为模型所需的格式（二维数组）
    features = np.array(data.features).reshape(1, -1)
    # 调用模型预测
    prediction = model.predict(features)
    # 返回预测结果（0/1/2对应鸢尾花类别）
    return {"class": int(prediction[0])}