import os
import shutil
from md2pdf.core import md2pdf
import git

def _get_repo(path):
    return git.Repo(path)

def _update_remotes(remotes):
    for remote in remotes:
        remote.fetch()
    print("Remotes updated")

def _get_remote_langauage_branches(branch):
    remote_branches = []
    for ref in branch('-r').split('\n'):
        remote_branches.append(ref.strip())
    all_lang_remote_branches = []
    for branch in remote_branches:
        if branch.startswith("origin/lang/"):
            all_lang_remote_branches.append(branch)
    return all_lang_remote_branches

def _get_documents(heads, checkout, branches):
    doc_path = os.path.abspath(os.path.join("..", "docs"))
    for branch in branches:
        print("Branch:", branch)
        local_name = branch.split("origin/")[-1]
        if local_name in heads:
            checkout(local_name)
        else:
            checkout('-t', branch)
        language_name = local_name.split("/")[-1].strip()
        pdf_path = os.path.abspath(os.path.join("..", language_name))
        if os.path.exists(pdf_path):
            shutil.rmtree(pdf_path)
        os.mkdir(pdf_path)
        files = os.listdir(doc_path)
        files.sort()
        print(files)
        mdcontent = ""
        for file in files:
            if ".md" in file:
                md_file_path = os.path.join(doc_path, file)
                with open(md_file_path, 'r') as f:
                    mdcontent += "\n".join(f.readlines())
        filename = "{}_a4kWs.pdf".format(language_name)
        destination = os.path.join(pdf_path, filename)
        md2pdf(destination, md_content=mdcontent)
        print("Created ", destination)
    checkout('master')



def main():
    repo = _get_repo("..")
    _update_remotes(repo.remotes)
    language_branches = _get_remote_langauage_branches(repo.git.branch)
    _get_documents(repo.heads, repo.git.checkout, language_branches)
   
 


if __name__ == "__main__":
    main()