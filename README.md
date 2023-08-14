# stockscreener
Need the following 2 lines before making stockscreener object to work

COMMANDLINE1 = f'chrome.exe --remote-debugging-port={9999} --user-data-dir="DIRECTORY_OF_LOCAL_HOST"'
subprocess.Popen(COMMANDLINE1, shell=True, cwd=DIRECTORY_OF_YOUR_GOOGLE_CHROME_EXE)
