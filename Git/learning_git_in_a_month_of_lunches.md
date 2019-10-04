# git ls-files
���|�W�g���ŊǗ�����Ă���t�@�C���̈ꗗ���擾����

git ls-files

#git log
�R�~�b�g�̗������m�F����

git log --oneline
git log --stat

#git blame
�t�@�C�����e(&�C������)���m�F

git blame readme.txt

#git config
�ݒ���m�F����A�ύX����

git config --list
git config --global user.name "wuxi2000"
git config --global user.email "wuxi2000@gmail.com"

#git help
�w���v��\������

git help help
git help glossary
git help -a
git help config
git help -p

#git add
��ƃG���A�̃t�@�C�����X�e�[�W���O�G���A�ɒǉ�����

git add readme.txt
git add .
git add --dry-run readme.txt

#git check-out
�|�C���^���ړ�����ƂƂ��ɁA���|�W�g���ł̃t�@�C������ƃt�H���_�ɔ��f
1. ����u�����`���ɁA�|�C���^���ړ�����
1. �قȂ�u�����`�ȈՁA�|�C���^���ړ�����
    
                 feature
                 ��
         A---B---C
        /                    
    0---1
       ��
        master (*)

checkout feature
checkout 
    
#git reset

#git branch
�u�����`����

git branch
git branch -v # version SHA1��\������


#git commit
�R�~�b�g����

git commit -m "commit message ..."
git commit --amend -m "change commit message of last commit ..."

#git diff
��r����

git diff # ��ƃG���A vs �X�e�[�W���O�G���A
git diff --staged # �X�e�[�W���O�G���A vs ���|�W�g��

#UI tool
UI �c�[�����J��

git citool
git gui
gitk # git log �ɑΉ�������

GUI �őS�u�����`��\������
Gitk view definition -- criteria for selecting reversions
