# simple-screenshot-taker
Screenshot taker in python for Windows users. Fast parental supervision.

## Requirements
`pip install PyAutoGUI`

## How to run
### Firsth possibility
Just click 2 times on **run.pyw**
### Second possibility (Recommended)
Add **run.pyw** to autostart. In Win10:
1. Press **Windows+R**.
2. Type "shell:startup" and press enter.
3. Add there paste a **shortcut** to run.pyw.
**IMPORTANT! DO NOT PASTE THERE run.pyw!** Application is creating pictures in folder where is. So paste there **only a shortcut to application**.

## Config
There is two possible options:
1. Interval - How long application will wait untill take another screenshot (in seconds).
2. Counter - How many screenshots should take (working time = interval * counter).

Interval and counter default options in 60. So application will work 3600 seconds = 60 minutes = 1 hour.
If you wanna change it feel free to open application in any text editor and change variables on line **6** and **7**.

#### I hope this has helped someone 😊
#### Made with ❤️ by LityS