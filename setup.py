import sys
from cx_Freeze import setup, Executable

executables = [Executable("ChatbotInterface.py", base=None)]

build_exe_options = {
    "packages": [],
    "excludes": [],
    "include_files": [],
}

setup(
    name="Chatbot",
    version="1.0",
    description="Rasa Chatbot",
    options={"build_exe": build_exe_options},
    executables=executables,
)
