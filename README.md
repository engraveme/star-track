<div align="center">
需要参考：
[github webhooks](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks)
[uv Python](https://blog.csdn.net/2401_86720553/article/details/156489207)
[githubapi](https://pygithub.readthedocs.io/en/)
[gitpython](ttps://gitpython.readthedocs.org)
[git diff](https://www.cnblogs.com/uncleyong/p/17967981)
[Claude Code](https://blog.csdn.net/qq_20042935/article/details/157643418)
[huggingface_hub](https://blog.csdn.net/asdurt/article/details/155452779)

# Let your code changes get reviewed by AI with codereview-agi

</div>

<div align="center">
  
![ezgif-5-956a1609ab](https://github.com/fynnfluegge/gitreview-gpt/assets/16321871/ce68fb34-2748-4929-aaaa-b2a1271301a5)

</div>

Get review suggestions to changes in your git working directory or to any committed changes in your current branch against a target branch and let these suggestions get applied to your code
with an informative commit message.

## ✨ Features

- **Get feedback and suggestions with the corresponding line numbers to your git changes in your terminal**
- **Let your current working directory get reviewed (staged and unstaged changes)**
- **Let all commits of your current branch get reviewed against any specific target branch**
- **Let AI-generated review suggestions get applied to your code**
- **Let a commit message get generated for your current changes**

> [!NOTE]
> Review suggestions will only be applied to files without unstaged changes, so that nothing is overridden.

## 🚀 Usage

- `rgpt review`: Reviews all changes in your working directory and applies review suggestions to related files autonomously.
- `rgpt review --readonly`: Reviews all changes without applying the suggestions to the code.
- `rgpt review --guided`: User needs to confirm review process for each file. Useful if not all files should get reviewed.
- `rgpt review --target $BRANCH`: Reviews all committed changes in your current branch compared to `$BRANCH`.
- `rgpt review --gpt4`: Use GPT-4 model (default is GPT-3.5).
- `rgpt commit`: Generates a commit message for your staged changes.

## 📋 Requirements

python -m gitreview_gpt review - 审查工作目录中的所有变更并自动应用建议
python -m gitreview_gpt review --readonly - 只审查不应用建议
python -m gitreview_gpt review --guided - 每个文件都需要确认
python -m gitreview_gpt review --branch main - 审查当前分支相对于 main 分支的所有提交
python -m gitreview_gpt commit - 为暂存的变更生成提交信息

## 🔧 Installation

Create your personal OpenAI Api key and add it as `$OPENAI_API_KEY` to your environment:

```
uv pip install -e .
```

Install with `pipx`:

```
pipx install gitreview-gpt
```
> [!NOTE]
> It is recommended to use `pipx` for installation, nonetheless it is also possible to use `pip`.
