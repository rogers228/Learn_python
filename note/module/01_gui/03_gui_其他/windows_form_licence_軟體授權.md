## windows form licence 軟體授權

以下是我的規劃實現 user單裝置限制，以裝置deviceid及 licence實現：他不使用table, Policy
1. gui forms初始化實建立uuid作為deviceid
2. 做一個table user_device，登入後新增或更新 userid, deviceid(userid只會有一個deviceid)
3. 做一個到期日，例如30日後到期，到期後將會出現提示輸入licence，未通過驗證無法使用主要功能。
4. 做一個輸入licence表單，可以請求發送licence，及輸入licence執行驗證。
5. 系統為driveid建立licence儲存在user_drive.licence，並發信給user。
6. 以deviceid 驗證licence合法即可使用，未通過驗證無法使用主要功能。
7. 相同使用者的就裝置，因為driveid不同，將無法使用主要功能。