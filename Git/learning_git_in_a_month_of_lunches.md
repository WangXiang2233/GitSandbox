# git ls-files
リポジトリで管理されているファイルの一覧を取得する

git ls-files

# git log

コミットの履歴を確認する

git log --oneline
git log --stat

# git blame
ファイル内容(&修正履歴)を確認

git blame readme.txt

# git config
設定を確認する、変更する

git config --list
git config --global user.name "wuxi2000"
git config --global user.email "wuxi2000@gmail.com"

# git help
ヘルプを表示する

git help help
git help glossary
git help -a
git help config
git help -p

# git add
作業エリアのファイルをステージングエリアに追加する

git add readme.txt
git add .
git add --dry-run readme.txt

# git check-out
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
    
# git reset

# git branch
ブランチ操作

git branch 
git branch -v # version SHA1を表示する
git branch feature # featureというブランチを作る


# git commit
コミットする

git commit -m "commit message ..."
git commit --amend -m "change commit message of last commit ..."

# git diff
比較する

git diff # 作業エリア vs ステージングエリア
git diff --staged # ステージングエリア vs リポジトリ

# git push
ローカルからリモートにプッシュする


git push -u origin feature1 # リモート：origin / ローカル：feature1 
git push # 現在のブランチと同名のブランチがリモートに既に存在する場合に使う

# git pull
リモートからローカルへプルする

git pull

# git stash
他ブランチをマージする前に、作業エリアとステージングエリアにある編集中のファイルを一時退避

git stash
git stash list
git stash pop

# git log

git log --graph --decorate --pretty=oneline --all --abbrev-commit

# git diff

git diff master...feature
git diff --name-status master...feature # ファイル名だけを表示

# UI tool
## UI ツールを開く
git citool
git gui
gitk # git log に対応する画面

## GUI で全ブランチを表示する
gitk -> (MENU) View -> New View -> All (local) branches -> Remember this view

## Mergetool

git mergetool

