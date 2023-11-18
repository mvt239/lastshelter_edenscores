# Last Shelter: Survival - Eden Score Extractor

Small OCR script to loop through player scores, and output to csv. 
Update the first to variables to match your needs. This relies on a directory of screenshots for individual players scores and outputs as:


```
user_id,contribution,ranking,season_points,eden_demolition,eden_feat,occupy_enemy_territory
black,288923,1,30656,576289,22886732226,586
```
Doesn't always do well with players that have special characters in their name, be sure to double check.


Relies on tesseract OCR:

For Mac:
```
brew install tesseract
```
Nix/Ubuntu:
```
sudo apt update
sudo apt install tesseract-ocr
```


<a href="https://www.buymeacoffee.com/mvt239" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
