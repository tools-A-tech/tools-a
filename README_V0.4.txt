ProductSiteCMS V0.4

【変更内容】
・HTML内の siteInfo を削除
・HTML内の noticeInfo を削除
・data/siteinfo.json を追加
・js/siteinfo-loader.js を追加
・サイト名、説明、更新情報、SNS、支払い方法、注意事項、問い合わせURLをJSON管理化
・V0.1 products.json / V0.2 games.json / V0.3 faq.json はそのまま維持

【Win7 IISへの設置】
このフォルダ内の以下を C:\inetpub\wwwroot\ へ上書きコピーしてください。

index.html
data フォルダ
js フォルダ

【配置後の確認】
1. http://192.168.11.17/data/siteinfo.json
2. http://192.168.11.17/js/siteinfo-loader.js
3. http://192.168.11.17/ を Ctrl + F5 で更新
4. 「お問い合わせ前にお読みください」を開き、更新情報・SNS・支払い方法を確認
5. 「注意事項」を開き、本文が表示されることを確認
6. 商品ポップアップのX・LINEボタンが開くことを確認

【siteinfo.json の主な項目】
siteName        : サイト名
siteDescription : サイト説明
updateInfo      : 更新情報（HTML使用可）
snsInfo         : SNS情報（HTML使用可）
paymentInfo     : 支払い方法（HTML使用可）
noticeInfo      : 注意事項
contact.xUrl    : X問い合わせURL
contact.lineUrl : LINE問い合わせURL
