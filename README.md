# Gasbar
## Ethereum Gas Fee for the MacBook Pro touchbar (using BetterTouchTool)

Worried about Ethereum gas fees? Me too. I'd like to keep an eye on them so I know when to ape into some foodcoin that's gonna get rugpulled tomorrow anyway.

Now you can, look! **L**(ow) | **A**(verage) | **H**(igh) gas fees, in gwei! 

![](https://raw.githubusercontent.com/tssandor/gasbar/main/readmemd_images/gasbar_photo.png)

**What magic is this you ask?**

[BetterTouchTool](https://folivora.ai/). It's an app that makes your MacBook Pro touchbar actually useful as you can add custom scripts like crypto prices and now, gas. It costs money but it's worth it. Also comes with a free trial.

## Oke how do I set this up?

### 1. Download BetterTouchTool
[You'll need it.](https://folivora.ai/)

### 2. Clone this repo
Or just grab the gasbar.py file, you don't need anything else

### 3. Configure Python
`pip3 install requests`, as we need this module to run the script. It's `pip3` unless you have Python3 globally (unlikely).

### 4. Get an Etherscan API key
No dirty webscraping workarounds here, we do this the correct way. Register a user on [Etherscan](https://etherscan.io) and [create an API key](https://etherscan.io/myapikey).

### 5. Add the script to BetterTouchTool
- Type `Shell Script / Task`
- Launch path: `/usr/bin/python3`
- Parameters: `-c`
- Environment variables: `ETHERSCAN_TOKEN=` and your token (no quotation marks needed)
- Script: copy-paste the contents of `gasbar.py`

![](https://raw.githubusercontent.com/tssandor/gasbar/main/readmemd_images/bettertouchtool.png)

### 6. Fine tune it
- Execute the script every x seconds (I prefer 60 but up to you)
- Select a nice background color, etc

## Done. Enjoy <3