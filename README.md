# 遠端LED控制器


## 組員分工

- 張逸于(資工二 105213029) 部分code 延伸輸入端部分及PPT內容
- 周沛群(資工二 105321042) 部分cdoe 字元table
- 張以箴(資工二 105321020) 部分code 及PPT美化
- 白 薇(資工三 106321402) 資料彙整及使用者端連接

## 想法

讓用戶可以在遠端控制LED輸出內容。如果今天在房間裡面，不想要被打擾，或是忙完了可以被打擾，只要敲敲鍵盤，就能把使用者現在的狀態讓門外的客人或是過路客知道，降低敲門又沒人回應，或是在不對的時機打擾到他人的機率。

## 原理

ssh連線到pi 在pi上面執行程式讓LED秀出內容
延伸：架一個簡單的網頁提供用戶輸入，讓用戶可以在瀏覽器就更新LED狀態

## 示意圖

![](https://i.imgur.com/baIfnf4.png)

## 器材
- 8x8LED點矩陣
- Raspberry Pi

## 參考資料

[LED code](https://github.com/adafruit/Adafruit_Python_LED_Backpack/blob/master/examples/matrix8x8_test.py)
