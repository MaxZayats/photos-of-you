# photos-of-you — App for taking photos from a webcam

# Installation
1. You need Python version 3.7+ <br>
   You can install Python here: https://www.python.org/
2. ```git clone https://github.com/MaxZayats/photos-of-you```
3. ```cd photos-of-you```
4. ```pip install -r requirements.txt```
5. Installation is complete.

# Usage
1. To start using the app, you need to expose your local web server.<br>
   **You need a secure Protocol to use the app!(htpps)**<br>
   You can do this in the following ways:
   * https://localhost.run/ -> ```ssh -R 80:127.0.0.1:5000 ssh.localhost.run```
   * https://serveo.net/ -> ```ssh -R 80:127.0.0.1:5000 serveo.net```
   * https://ngrok.com/ <br>
     and others...<br>
2. You can change the template "**template.html**" to your template.
3. Run "app.py"<br>
   ```python3 app.py```
4. The photos will be saved in the "photos" folder.
