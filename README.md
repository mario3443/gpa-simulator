# gpa-simulator - GPA 成績模擬計算器

## 學習背景

這個專案是我想深入學習CLI工具開發時做的練習作品。之前有做過一個簡單的CLI專案，但覺得還不夠熟悉，就想做一個比較有結構、能處理檔案的模擬器來加強練習。剛好自己平常也會算GPA，所以就決定做這個GPA模擬器，當作實作練習用。

## 功能介紹

- 可以輸入課程、學分和成績來計算目前所擁有的GPA

![image](https://github.com/user-attachments/assets/e3e3c41d-bab2-474d-801e-52fefb29ceab)

- 可以觀看和刪除目前所設置之課程

![image](https://github.com/user-attachments/assets/e834e67f-537b-4786-b4ee-c0308a3c4581)

![image](https://github.com/user-attachments/assets/1a8e6361-6ff6-479f-b425-7f15431bb81c)

- 可以模擬如果某科成績改變後的狀況

![image](https://github.com/user-attachments/assets/f99b554b-6394-49fa-8591-6062eafea362)

- 會將檔案存入json檔案中，重開後照樣存在

![image](https://github.com/user-attachments/assets/50a2e400-cdc3-47d7-967c-bdc08e6f0ffc)

- 支援使用導入ChatGPT來分析目前課表，來給你建議（需要設定API金鑰）

![image](https://github.com/user-attachments/assets/c165dab9-6fb3-4792-918c-0c98c3c1676e)

## 如何使用

先clone此專案到你的資料夾當中

然後設置一個檔案為.env後放入以下資訊

```
chatgpt_apikey = 你的chatgpt_apikey
```

隨後即可以啟動python主程式

```python main.py```

## 學習或利用到的程式

### Python (用來製作CLI的介面）

### json （用來編輯和儲存成績資料）

### openai-api （用來連接chatgpt去評論成績）
