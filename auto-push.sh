#!/bin/bash

# 自动提交并推送当前目录下的所有修改

# 提交信息，带时间戳
commit_msg="auto commit on $(date '+%Y-%m-%d %H:%M:%S')"

# 添加所有更改
git add .

# 提交
git commit -m "$commit_msg"

# 推送到远程 main 分支（如果是 master 改成 master）
git push origin main
