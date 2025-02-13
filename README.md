## Setup Instructions

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```sh
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Create a Virtual Environment

You can create a virtual environment using Python's built-in `venv` module.

#### If `python3` is your default Python version:
```sh
python3 -m venv .venv  # Creates a virtual environment in a folder named .venv
```

#### If `python3` is NOT your default Python version:
```sh
python -m venv .venv
```

### 3. Activate the Virtual Environment

Run the following command based on your operating system:

#### On macOS/Linux:
```sh
source .venv/bin/activate
```

#### On Windows (Command Prompt):
```sh
.venv\Scripts\activate
```

#### On Windows (PowerShell):
```sh
.venv\Scripts\Activate.ps1
```

### 4. Deactivate Conda Environment (If Needed)

If you are using Conda and need to deactivate it before proceeding, run:
```sh
conda deactivate
```

### 5. Install Dependencies

With the virtual environment activated, install the required dependencies:
```sh
pip install -r requirements.txt
```

### 6. Run the Application

To start the Streamlit app, run:
```sh
streamlit run app.py
```

[App Link](https://techresumeapp.streamlit.app/)
