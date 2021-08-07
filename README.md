# VSRG Conversion Tool
A converter for many VSRG formats made with [reamberPy](https://github.com/Eve-ning/reamberPy).

## NOTICE
- I couldn't check the BMS file, as do not have the means to do so currently.
- Conversion to StepMania requires you to then shift the offset by a couple of measures.
- Conversion to Quaver seems to be a problem currently. 
  
- This will need an overhaul in the future when the new version of reamberpy is released.

## What and Why
VSRG stands for Vertical Scrolling Rhythm Game. 

This family of game consists of many games which have their own file formats implemented.
The goal of this is to provide a simple way to convert between these games.

Currently supported formats are:
- osu!mania (.osu)
- Quaver (.qua)
- StepMania (.sm)
- BMS (.bms)

## How to install
Please have Python 3.7 or later installed

After that, you can install all the requirements via `pip install -r requirements.txt`.
Then for now, you can use `main.py` to convert between file formats

## TODO
- GUI
- Fix Quaver conversion
