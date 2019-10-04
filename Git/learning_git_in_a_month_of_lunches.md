# git ls-files
リポジトリで管理されているファイルの一覧を取得する

git ls-files

#git log
コミットの履歴を確認する

git log --oneline
git log --stat

#git blame
ファイル内容(&修正履歴)を確認

git blame readme.txt

#git config
設定を確認する、変更する

git config --list
git config --global user.name "wuxi2000"
git config --global user.email "wuxi2000@gmail.com"

#git help
ヘルプを表示する

git help help
git help glossary
git help -a
git help config
git help -p

#git add
作業エリアのファイルをステージングエリアに追加する

git add readme.txt
git add .
git add --dry-run readme.txt

#git check-out
ポインタを移動するとともに、レポジトリでのファイルを作業フォルダに反映
1. 同一ブランチ内に、ポインタを移動する
1. 異なるブランチ簡易、ポインタを移動する
    
                 feature
                 ↓
         A---B---C
        /                    
    0---1
       ↑
        master (*)

checkout feature
checkout 
    
#git reset

#git branch
ブランチ操作

git branch
git branch -v # version SHA1を表示する


#git commit
コミットする

git commit -m "commit message ..."
git commit --amend -m "change commit message of last commit ..."

#git diff
比較する

git diff # 作業エリア vs ステージングエリア
git diff --staged # ステージングエリア vs リポジトリ

#UI tool
UI ツールを開く

git citool
git gui
gitk # git log に対応する画面

GUI で全ブランチを表示する
Gitk view definition -- criteria for selecting reversions
