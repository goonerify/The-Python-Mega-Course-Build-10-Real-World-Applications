## Windows Commands

Find where a program is installed (equivalent of `which` command in linux)\
Command line: `where <program name>` `where /?` (for help)\
Powershell: `Get-Command <program name>`

## PYTHON COMMANDS

[Create new virtual environment](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html#create-a-virtual-python-environment)
[Create new virtual environment with VS Code](https://stackoverflow.com/a/61092957/1445318)

`python -m venv <reference a name for your virtual environment i.e venv.test.numpy>`

<!---
Important: Always give your venv a unique name so that you always know which is active
-->

Activate virtual environment from directory with virtual environment
`.\<venv name>\Scripts\activate`

Create requirements.txt file
`pip freeze > requirements.txt`

Install 3rd party package with pip
`pip3 install pandas`

Get all properties and methods of an object
`dir <object name>`

## JUPYTER NOTEBOOK COMMANDS

[Change Jupyter notebook startup directory](https://stackoverflow.com/a/40514875/1445318)
or just [Open the notebook in any directory](https://stackoverflow.com/a/39453881/1445318)

[Add a new kernel to your Jupyter config from command line](https://stackoverflow.com/a/49309403/1445318)

[Add a new kernel to your Jupyter config from command line: 2](https://janakiev.com/blog/jupyter-virtual-envs/)

### JUPYTER NOTEBOOK NEW PROJECT SETUP

1. Activate virtual environment
   a. `<path to activate.bat>` i.e `venv\Scripts\activate` OR
   b. `conda activate <venv name>`
2. install ipykernel which provides the IPython kernel for Jupyter
   `pip install ipykernel`
3. Add your virtual environment to Jupyter from your project directory
   `python -m ipykernel install --user --name=<any name to reference kernel, usually the venv name>`

   This should print something like:<code>Installed kernelspec myenv in <i>/home/user/.local/share/jupyter/kernels/myenv</i></code>

   In this folder you will find a <i>kernel.json</i> that points back to the local virtual environment for your project

4. Install dependencies
   `pip install -r requirements.txt`
5. Start new jupyter session (from a command prompt )
   `jupyter notebook`

   In jupyter notebook (reload if necessary), `kernel -> Change kernel -> "Reference kernel name"`

### Other Jupyter commands

1. Delete a jupyter notebook kernel
   `jupyter kernelspec uninstall <Reference kernel name>`

### Jupyter Python Commands

1. List all files in current directory
   ```
   import os
   os.listdir()
   ```
2. Get help info for an object
   Append a question mark i.e `pandas.read_csv?`

### Jupyter useful shortcuts to add

move cell up: `Ctrl-Up` \
move cell down: `Ctrl-Down`
