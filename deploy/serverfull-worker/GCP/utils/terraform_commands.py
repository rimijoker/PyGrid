"""Helper methods to wrap terraform script/notbook commands"""
import IPython
from notebook import terraform_notebook
from script import terraform_script


def init():
    """
    Runs terraform init
    """
    if IPython.get_ipython():
        terraform_notebook.init()
    else:
        terraform_script.init()


def apply():
    """
    Runs terraform apply
    """
    if IPython.get_ipython():
        terraform_notebook.apply()
    else:
        terraform_script.apply()


def destroy():
    """
    Runs terraform destroy
    """
    if IPython.get_ipython():
        terraform_notebook.destroy()
    else:
        terraform_script.destroy()
