# New Russian wine

## Project Description
 - Website of the author's wine store "New Russian wine".

## Technologies and tools
 - Python
 - HTML
 - JavaScript
 - CSS

## How to use
1. Clone this repository and go to the project folder:
   ```bash
   cd /c/project_folder # for example
   ```
   ```bash
   git clone https://github.com/JacobKleim/Wine
   ```
   ```bash
   cd /c/project_folder/Wine 
   ```

2. Create a .env file with parameters:
   ```
   PATH_DRINKS_FILE=path to the drinks file
   ```


3. Сreate and activate a virtual environment:
   ```
   python -m venv venv
   ```
   ```bash
   source venv/Scripts/activate
   ```

4. Install dependencies:
   ```
   python -m pip install --upgrade pip
   ```
   ```
   pip install -r requirements.txt
   ```


5. Create an Excel table and fill it in with your data according to the provided sample:
| Category | Drink name | sort | price | image | promotion |
|----------|-------------|-----------|-------|-----------------|-----------------|
| Category | Kindzmarauli | Saperavi | 100$  | kindzmarauli.png | Profitable proposition |


6. Start the project:
   When running the project, specify the path to the directory where your Excel file is stored:
   ```
   python main.py -f /c/wine.xlsx (indicate your path to the file)
   ```
   or specify the path in the PATH_DRINKS_FILE environment variable in the .env file and run the project:
   ```
   python main.py
   ```
   open the website http://127.0.0.1:8000/index.html


## Example of work

![сайт вина шапка](https://github.com/JacobKleim/Wine/assets/119351169/d70737a0-759e-45ea-b6e0-fa1293197efb)

![сайт вина ассортимент](https://github.com/JacobKleim/Wine/assets/119351169/b6bdb2af-88df-4d86-be89-36f989ca714d)
