import os
import shutil
from md2pdf.core import md2pdf
import git
import tempfile

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

def _copy_css_to_tmp():
    css_file = os.path.abspath(os.path.join(".", "default.css"))
    tmp_path = os.path.join(tempfile.gettempdir(), "default.css")
    shutil.copyfile(css_file, tmp_path)
    return tmp_path

def _get_documents(heads, repo, branches):
    css_file = _copy_css_to_tmp()
    doc_path = os.path.abspath(os.path.join("..", "docs"))
    base_path = os.path.abspath(os.path.join(".."))
    for branch in branches:
        print("Branch:", branch)
        local_name = branch.split("origin/")[-1]
        if local_name in heads:
            repo.git.checkout(local_name)
        else:
            repo.git.checkout('-t', branch)
        repo.remotes.origin.pull("/".join(branch.split("/")[1:]))
        language_name = local_name.split("/")[-1].strip()
        pdf_path = os.path.abspath(os.path.join(base_path, language_name))
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
                mdcontent += "\n"
        filename = "{}_a4kWs.pdf".format(language_name)
        destination = os.path.join(pdf_path, filename)
        md2pdf(destination, md_content=mdcontent, css_file_path=css_file)
        print("Created ", destination)
    repo.git.checkout('master')
    os.remove(css_file)



def main():
    repo = _get_repo("..")
    _update_remotes(repo.remotes)
    language_branches = _get_remote_langauage_branches(repo.git.branch)
    _get_documents(repo.heads, repo, language_branches)
   
 


if __name__ == "__main__":
    main()