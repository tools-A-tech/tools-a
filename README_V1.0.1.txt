ProductSiteCMS V1.0.1
GitHub初期接続版

接続先:
https://github.com/tools-A-tech/tools-a
Git URL:
https://github.com/tools-A-tech/tools-a.git

【手順1】
V1.0.1の中身を次へ上書きします。

C:\inetpub\wwwroot\

【手順2】
現在開いているProductSiteCMS APIの黒い画面を閉じます。

【手順3】
次を右クリックし、「管理者として実行」します。

C:\inetpub\wwwroot\server\setup_github_connection.bat

処理内容:
・現在のwwwrootをバックアップ
・GitHubリポジトリをoriginへ登録
・GitHubの既存履歴を取得
・現在のCMSファイルを重ねて復元
・commit
・push

バックアップ先:
C:\inetpub\ProductSiteCMS_backup_before_github

最後に次が表示されれば成功です。

[OK] GitHub connection completed.

【pushだけ失敗した場合】
GitHub認証を完了した後、次を実行します。

C:\inetpub\wwwroot\server\test_github_push.bat

【手順4】
APIを再起動します。

C:\inetpub\wwwroot\server\start_api.bat

【手順5】
管理画面をCtrl+F5で更新します。

http://192.168.11.17/admin/

次の表示になれば完成です。

● Win7 API接続中
● GitHub接続準備済み (main)

【今後】
管理画面で編集後、

保存してGitHub公開

を押すだけで、Win7保存とGitHub Pages公開を実行します。
