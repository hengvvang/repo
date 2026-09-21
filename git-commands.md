# 常用 Git 命令

## 查看状态

```powershell
git status
```

查看当前分支、工作区、暂存区和未跟踪文件。

## 查看修改

```powershell
git diff
```

查看工作区中尚未暂存的修改。

```powershell
git diff --cached
```

查看暂存区中准备提交的修改。

## 保存修改

```powershell
git add <文件名>
```

将指定文件的修改放入暂存区。

```powershell
git commit -m "描述本次修改"
```

将暂存区内容保存为一次提交。
