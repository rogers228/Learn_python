# user單裝置限制_以Policy實現
1. 建立一個table user_sessions，登入後更新user_sessions。
2. 以直接目標table例如'rec_pd'的Policy設定，連接user的sessions(暫不討論完整的sql語法)，就能夠阻擋操作table的動作。

