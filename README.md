# Intro 
TLDR; This is Virus Total (https://www.virustotal.com/) extension for Nautilus (Gnome file manager on Linux) If you download files and don't have antivirus then this can be used as poor's man AV. After installing extension, select file & Righ-Click-->Properties->Virus_Total. You'll see reports like these:
![NotFound](https://github.com/shvechkov/nautilus_virustotal/blob/master/vtreport_notfound.png?raw=true)

![OK](https://github.com/shvechkov/nautilus_virustotal/blob/master/vtreport_ok.png?raw=true)

![Flagged](https://github.com/shvechkov/nautilus_virustotal/blob/master/vtreport_flagged.png?raw=true)


# Details 
The extension is written in python and uses python bindings for Nautilus extension framewiork(see https://wiki.gnome.org/Projects/NautilusPython)

Extension calculates md5 hash of a file and call VirusTotal REST API to get info (AV scan report)

For plugin to work you first need to get valid API KEY from Visrus Total (create account and get your key for free - see this https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key ) Then add the follwoing into your ${HOME}/.bashrc
`export VIRUS_TOTAL_API_KEY=<your_actual_key>`


## Instructions for Ubuntu 22.04.3 LTS 

`git clone git clone git@github.com:shvechkov/nautilus_virustotal.git && source ${HOME}/.bashrc && cd nautilus_virustotal && install.sh`

- above gets gets repo with extension file, sets API Key variable and installs extension






