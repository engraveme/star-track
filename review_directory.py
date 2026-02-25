"""
审查指定目录下的代码
支持 Git 仓库和非 Git 目录
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path


def is_git_repo(directory):
    """检查目录是否是 Git 仓库"""
    git_dir = Path(directory) / ".git"
    return git_dir.exists()


def has_git_changes(directory):
    """检查是否有 Git 变更"""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=directory,
            capture_output=True,
            text=True,
            check=True
        )
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False



def run_review(directory, readonly=False, guided=False, branch=None):
    """运行代码审查"""
    # 构建命令
    cmd = [sys.executable, "-m", "gitreview_gpt", "review"]
    
    if readonly:
        cmd.append("--readonly")
    if guided:
        cmd.append("--guided")
    if branch:
        cmd.extend(["--branch", branch])
    
    print(f"\n🔍 开始审查代码...")
    print(f"📂 目录: {directory}")
    print(f"🚀 命令: {' '.join(cmd)}\n")
    
    try:
        subprocess.run(cmd, cwd=directory, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 审查失败: {e}")
        return False
    except KeyboardInterrupt:
        print("\n\n⚠️  审查被用户中断")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="审查指定目录下的代码",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 审查指定目录（只读模式）
  python review_directory.py D:\\project\\yx-master\\yxdd-intretech\\ddtalk --readonly
  
  # 审查并应用建议（引导模式）
  python review_directory.py D:\\project\\yx-master\\yxdd-intretech\\ddtalk --guided
  
  # 审查相对于指定分支的变更
  python review_directory.py D:\\project\\yx-master\\yxdd-intretech\\ddtalk --branch main
        """
    )
    
    parser.add_argument(
        "directory",
        help="要审查的目录路径"
    )
    parser.add_argument(
        "--readonly",
        action="store_true",
        help="只读模式，不应用审查建议"
    )
    parser.add_argument(
        "--guided",
        action="store_true",
        help="引导模式，每个文件都需要确认"
    )
    parser.add_argument(
        "--branch",
        type=str,
        help="审查相对于指定分支的变更"
    )
    parser.add_argument(
        "--no-init",
        action="store_true",
        help="如果不是 Git 仓库，不自动初始化"
    )
    
    args = parser.parse_args()
    
    # 检查目录是否存在
    target_dir = Path(args.directory).resolve()
    if not target_dir.exists():
        print(f"❌ 目录不存在: {target_dir}")
        sys.exit(1)
    
    if not target_dir.is_dir():
        print(f"❌ 路径不是目录: {target_dir}")
        sys.exit(1)
    
    print(f"=" * 60)
    print(f"  代码审查工具")
    print(f"=" * 60)
    
    # 检查是否是 Git 仓库
    # is_git = is_git_repo(target_dir)
    
    # if not is_git:
    #     print(f"⚠️  目录不是 Git 仓库: {target_dir}")
    #     sys.exit(0)
    # else:
    #     print(f"✅ 检测到 Git 仓库")
    if not has_git_changes(target_dir) and not args.branch:
        print("⚠️  没有检测到代码变更")
        print("💡 提示: 使用 --branch 参数来审查相对于某个分支的提交")
        sys.exit(0)
    
    # 运行审查
    success = run_review(
        target_dir,
        readonly=args.readonly,
        guided=args.guided,
        branch=args.branch
    )
    
    print("\n✨ 完成!")


if __name__ == "__main__":
    main()
