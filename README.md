# FrameExtractor

Save user defined number of images from video. 

![ExtractFrames](https://github.com/user-attachments/assets/4888ba64-6dc0-4209-9d29-0d44059a2bea)





# How to Run

### Method 1.

Download the parts inside [/Complete With Ffmpeg/](https://github.com/noarche/FrameExtractor/tree/main/Complete%20with%20ffmpeg)

Download [Winrar](https://www.rarlab.com/download.htm) & extract to `C:/extractFrames`

Download [python](https://www.python.org/downloads/)

Install python and add to path during installation

![image](https://github.com/user-attachments/assets/51410975-265d-4bb6-9fe8-9415ad2d4e53)


Press windows key + R and type `cmd` then press enter to open terminal

in terminal type `cd C:/extractFrames`

Command to run `python ExtractFrames.py`


### Method 2

Download the parts inside [/Complete With Ffmpeg/](https://github.com/noarche/FrameExtractor/tree/main/Complete%20with%20ffmpeg)

Download [Winrar](https://www.rarlab.com/download.htm) & extract to `C:/extractFrames`

Run the .exe file that is in the same directory as ffmpeg.exe

## Extracting Frames

Input number of images to save

Drag video file to the terminal window and delete the quotations around file path if your OS adds them. 

Press enter to finish.  Look inside the root dir (where ExtractFrames.py is located) for a new directory with images. A new Directory will be created for each video so the images are not mixed. 



## 🛡️ Is this a virus❔

No it is not a virus, that is a false positive. Anything compiled with pyinstaller will be flagged as potentially malicious. Pyinstaller is what turns the .py file into a .exe file and allows people to run python scripts as portable applications without the need to install python or any dependancies.  

Please scan the actual source, the file that ends with '.py' -  It will with no doubt be 100% clean on virustotal.  That being said I have provided instructions on how to build your own exe from the file you know is clean. 


🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻

🛡️ Tip for all questionable applications: 

*Running the application via [Sandboxie](https://sandboxie-plus.com/downloads/) or similar app will virutalize and protect your OS as if it was running on a virtual machine - [Sandboxie](https://sandboxie-plus.com/downloads/) can be used with any application or installation package thus another great tool to have.* 

🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺

## ꧁꧂ ✨ How to Compile your own .exe file❔ 

*You are able to build your own exe file from the source on a windows and linux machine. Follow the steps below, assuming you have already installed pip*

Clone this repo with git

    git clone https://github.com/noarche/FrameExtractor


Change to the directory containing the Python script
  	
    cd \FrameExtractor\

Run the following command to use pyinstaller to build an executable from the souce. Verify your version # in command matchs the version in source  dir. 
     
     pyinstaller --onefile FrameExtractor.py

Pyinstaller will created a couple of directories and files. 

    The .exe you want is located in \source\dist\FrameExtractor.exe


# ꧁꧂  Buy me a coffee ☕

![qrCode](https://raw.githubusercontent.com/noarche/cd-ripper/main/unrelated-ignore/CryptoQRcodes.png)

**Bitcoin** address `bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j`


**Ethereum** address `0x94FcBab18E4c0b2FAf5050c0c11E056893134266`


**Litecoin** address `ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx`



-------------------------------------------------------------------

![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)

