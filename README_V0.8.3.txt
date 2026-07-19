ProductSiteCMS V0.8.3

【重要な修正】
APIはWin7で起動しています。

そのため、Win11のブラウザで

http://127.0.0.1:8765/api/status

を開くと、Win11自身へ接続します。
Win7のAPIには接続しません。

Win11から確認するときは、Win7のIPアドレスを使います。

http://192.168.11.17:8765/api/status

【設置】
V0.8.3の中身を次へ上書きします。

C:\inetpub\wwwroot\

【起動】
Win7で次をダブルクリックします。

C:\inetpub\wwwroot\server\start_api.bat

起動後、黒い画面に次が表示されます。

LOCAL TEST : http://127.0.0.1:8765/api/status
WIN11 TEST : http://192.168.11.17:8765/api/status
CMS        : http://192.168.11.17/admin/

少し待つと、APIが自分自身へ接続確認を行います。

[SELF TEST] API OK

と表示されれば、API本体は正常です。

【確認方法】
Win7自身のブラウザ:
http://127.0.0.1:8765/api/status

Win11のブラウザ:
http://192.168.11.17:8765/api/status

Win11では127.0.0.1を使わないでください。

【Win7では成功、Win11では失敗する場合】
WindowsファイアウォールがTCP 8765を遮断しています。

次を右クリックし、

管理者として実行

してください。

C:\inetpub\wwwroot\server\allow_port_8765_as_admin.bat

その後、start_api.batを再起動します。

【管理画面】
http://192.168.11.17/admin/

Ctrl+F5で再読み込みします。

上部が

● Win7 API接続中

となれば接続成功です。

【保存】
商品やタイトルを追加・編集・削除したあと、

サーバーへ保存

を押します。

次へ直接反映されます。

C:\inetpub\wwwroot\data\games.json
C:\inetpub\wwwroot\data\products.json
C:\inetpub\wwwroot\images\
