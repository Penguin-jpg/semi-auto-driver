# semi-auto-driver

## 介紹

使用 MediaPipe 進行抓取手勢資料，透過 TensorFlow 訓練 MLP。將預測的手勢透過簡易伺服器傳送給樹梅派來操控小車移動。

## 資料集

執行 `app.py`，按下 `k` 將會開始錄製手勢，配合數字鍵 0 ~ 5 來為圖片標記不同的 label

## 模型訓練

準備好資料集後，執行 `keypoint_classification.ipynb` 來訓練手勢辨識模型

## 使用方法

- 將小車連接至樹梅派，並在樹梅派中執行 `client.py`
  - 可能需要依照不同的小車調整 `driver.py` 的配置
- 連接相機並執行 `app.py`，對著相機擺出手勢即可操縱小車移動

## 參考資料

- [手勢辨識](https://github.com/kinivi/hand-gesture-recognition-mediapipe)
- [Python socket 教學](https://www.youtube.com/watch?v=3QiPPX-KeSc)
