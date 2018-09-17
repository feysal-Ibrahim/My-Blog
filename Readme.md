BAADEST PITCH
AUTHOR
FEYSAL IBRAHIM

Link To The Deployed Site
Site link:https://pitch-feysal.herokuapp.com/

DESCRIPTION
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

Prerequisites
Ubuntu Software
Python3.6
Postgres
python virtualenv
Setup/Installation Requirements
internet access
$ git clone https://github.com/feysal-Ibrahim/Baddas-pitch
$ cd /Baddas-pitch
$ python3.6 -m venv virtual (install virtual environment)
$ source virtual/bin/activate
$ python3.6 -m pip install -r requirements.txt (install all dependencies)
Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
then $ ./start.sh
How it works
A user needs to register
A user the needs to log in to vote and post pitches
Updates on Bugs
The application cannot be run in any version of python lower than 3.6 because you will come across many errors

CREDITS
SAM NGINGI,CYNTHIA KASAMBULI and BOYD NDONGA

Technologies Used
Python3.6
Flask framework
PostgreSQL
Bootstrap
Support and Contacts
In case You have any issues using this code please do no hesitate to get in touch with me through addictivefazman@gmail.com or leave a commit here on github.

License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

MIT License Copyright (c) FEYSAL IBRAHIM Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated files , to deal in the Software without restriction, including and without limitation the rights to use, copy, modify, publish, distribute, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.