### Description

Fully automated quizzes and tasks with automatic grading, which have been carefully designed in accordance with the chapters of the great "Python for Everybody" book.

---

### Installation

Update the software.
```
sudo apt update && sudo apt upgrade -y
```

Install python and pip (python package manager).
```
sudo apt install python3.8 python3-pip
```

Install virtualenv (python environments manager).
```
pip3 install virtualenv && source ~/.profile
```

Clone the repository and cd into it.
```
git clone https://github.com/mrguseinov/python.git && cd python
```

Create a new virtual environment and activate it.
```
virtualenv venv && source venv/bin/activate
```

Install the required packages.
```
pip install -r requirements.txt
```

---

### Usage

Activate the virtual environment if it's not active.
```
source venv/bin/activate
```

And run the jupyter lab.
```
jupyter lab
```

---

### WSL Error

*More info in the [Jupyter Notebook Docs](https://jupyter-notebook.readthedocs.io/en/stable/config.html).*

Create a config file:
```
jupyter notebook --generate-config
```

Disable launching browser by redirect file:
```
c.NotebookApp.use_redirect_file = False
```
