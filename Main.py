# from OpenCV import HydroEye
# from MainRelay import Relay
import os

def main():
    # TODO: Linux path
    # TODO: Connect .py association with Python, not a text editor
    flag = os.system("D:\OneDrive\hxxdrich17-PC\Coding\Hydro Project\OpenCV.py")
    flag1 = os.system("D:\OneDrive\hxxdrich17-PC\Coding\Hydro Project\MainRelay.py")
    if (flag == 0 and flag1 == 0):
        print("The script has been launched successfully.")
    else:
        print("The script could not start correctly.")

if __name__ == "__main__":
    main()

