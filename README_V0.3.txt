ProductSiteCMS V0.3

【変更内容】
・HTML内の faqData を削除
・data/faq.json を追加
・js/faq-loader.js を追加
・FAQ表示処理を faq.json 読み込み後に実行
・V0.1 products.json / V0.2 games.json はそのまま維持

【Win7 IISへの設置】
このフォルダ内の以下を C:\inetpub\wwwroot\ へ上書きコピーしてください。

index.html
data フォルダ
js フォルダ

【配置後の確認】
1. http://192.168.11.17/data/faq.json
2. http://192.168.11.17/js/faq-loader.js
3. http://192.168.11.17/ を Ctrl + F5 で更新
4. 「よくある質問」を開き、13件表示されることを確認

【faq.json の項目】
id       : FAQ ID
question : 質問
answer   : 回答
sort     : 並び順
visible  : true=表示 / false=非表示
