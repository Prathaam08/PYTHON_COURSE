# To create a virtual environment 
python -m venv myenv   # myvenu is folder name 

# To activate the virtual environment in vs code 
.\myenv\Scripts\Activate.ps1

# To activate the virtual environment in window powershell
myenv\Scripts\activate.bat

# To deactivate the virtual environment
deactivate 

# It will print all the packages installed in the device  
pip freeze

# This command will include all this packages in file 
pip freeze > requirement.txt

# To install all the packages from requirement.txt
pip install -r requirement.txt