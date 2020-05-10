import os, subprocess, platform, pymongo

python_ver = platform.python_version()
print('=========================================================================')
print('python version', python_ver)
print('=========================================================================')

mongo_ver = pymongo.version
print('=========================================================================')
print('pymongo version', mongo_ver)
print('=========================================================================')

# check for the appropriate versions
if python_ver > '3.6' and mongo_ver > '3':

    print('Python and Mongo check complete. \n')
    
    '''
    GETTING THE SYSTEM READY.
    '''
    
    # install virtualenv and create a venv
    os.system('python -m pip install virtualenv')
    # create a venv
    os.system('python -m virtualenv venv')
    # activate the venv
    os.system("cd venv\Scripts")
    os.system("activate")
    
    '''
    GET APPLICATION REQUIREMENTS AND START THE SERVER.
    '''

    # install the requirements
    os.system('pip3 install -r requirements.txt')
    # start the server
    os.system('python app.py')

    # deactivate the virtual env
    os.system("deactivate")

else:
    print("You need to have python version 3.6 or higher or mongo version 3.0 or higher.")

