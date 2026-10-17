# PythonAnywhere: paste the contents of this file into your web app's WSGI configuration file
# (Web tab > "WSGI configuration file"), and fix the two paths/keys below.
import os, sys
path = "/home/YOURUSERNAME/bni-ask-editor"      # folder where you unzipped the project
if path not in sys.path:
    sys.path.insert(0, path)
os.environ["BNI_ADMIN_KEY"] = "choose-a-long-admin-key"
os.environ["BNI_VIEWER_KEY"] = "choose-a-long-viewer-key"
from app import app as application  # noqa
