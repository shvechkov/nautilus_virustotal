# Intro 
This is Virus Total (https://www.virustotal.com/) extension for Nautilus (Gnome file manager on Linux) This can be used as poor's man AV. After installing extension, select file & Righ-Click-->Properties->Virus_Total. You'll see reports like these:

![NotFound](https://github.com/shvechkov/nautilus_virustotal/blob/main/reports.png?raw=true)


# Details 
The extension is written in python and uses python bindings for Nautilus extension framewiork(see https://wiki.gnome.org/Projects/NautilusPython)

Extension calculates md5 hash of selected file and calls VirusTotal REST API to get AV scan report for a given file.

For plugin to work you first need to get a valid API KEY from Visrus Total (create account and get your key for free - see this https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key ) Then add the following into your ${HOME}/.bashrc
`export VIRUS_TOTAL_API_KEY=<your_actual_key>`

## Instructions for Ubuntu 22.04.3 LTS 

`git clone git@github.com:shvechkov/nautilus_virustotal.git && source ${HOME}/.bashrc && cd nautilus_virustotal && ./install.sh`

- above gets gets repo with extension file, exports API Key variable and installs extension





