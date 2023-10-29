sudo apt-get install python3-nautilus -y
mkdir -p ~/.local/share/nautilus-python/extensions
cp virustotal-property-page.py ~/.local/share/nautilus-python/extensions 
nautilus --quit
nautilus &
