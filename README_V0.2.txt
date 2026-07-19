ProductSiteCMS V0.2

【変更内容】
・titleNames を index.html から撤去
・titleImageMap を index.html から撤去
・ゲームタイトル 109件を data/games.json へ移行
・js/games-loader.js を追加
・products.json の商品138件はV0.1のまま維持
・既存デザイン、FAQ、ミニゲーム、ポップアップは維持

【配置】
C:\inetpub\wwwroot\
  index.html
  data\products.json
  data\games.json
  js\products-loader.js
  js\games-loader.js

【上書き方法】
V0.2フォルダ内の index.html、data、js を wwwroot へ上書きコピーしてください。
IISでは .json のMIMEタイプ application/json が必要です（V0.1で設定済みなら追加作業不要）。

【確認URL】
http://192.168.11.17/data/games.json
http://192.168.11.17/js/games-loader.js
http://192.168.11.17/

トップページは Ctrl+F5 で強制再読み込みしてください。
