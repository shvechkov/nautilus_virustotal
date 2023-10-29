import hashlib
import subprocess
import json
import os

# A way to get unquote working with python 2 and 3
try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

from gi.repository import Nautilus, Gtk, GObject

class VTPropertyPage(GObject.GObject, Nautilus.PropertyPageProvider):
    def __init__(self):
        pass
    
    def get_property_pages(self, files):
        if len(files) != 1:
            return
        
        file = files[0]
        if file.get_uri_scheme() != 'file':
            return

        if file.is_directory():
            return

        filename = unquote(file.get_uri()[7:])

        self.property_label = Gtk.Label('Virus_Total')
        self.property_label.show()

        self.hbox = Gtk.HBox(homogeneous=False, spacing=0)
        self.hbox.show()

        label = Gtk.Label('VirusTotal_report:')
        label.set_selectable(True)
        api_key = os.getenv('VIRUS_TOTAL_API_KEY')
        key="x-apikey: " + str(api_key)
        #print(f"{key}")

        file_stats = os.stat(filename)

        msg = ""
        if api_key != None and 0!= file_stats.st_size:
            md5sum=hashlib.md5(open(filename,'rb').read()).hexdigest()
            report_url = "https://www.virustotal.com/gui/home/search" 
            url="https://www.virustotal.com/api/v3/files/" + md5sum 
        
            cmd_array = ['curl', '--request','GET','--url',url,'--header',key]
            json_object = json.loads(subprocess.check_output(cmd_array))

            msg += """
            This tab scans files using <a href='https://www.virustotal.com/gui/home/search'>VirusTotal</a> public API    
            See brief scan result below ..   
            """

            msg += """
            File's md5sum:\n""" +"\t" + md5sum + "\n"

            msg += """
            For detailed report copy/paste file's hash into search form at 
            <a href='https://www.virustotal.com/gui/home/search'>VirusTotal</a>        
            """

            if "data" in json_object: 
                pref = ""
                suff = ""
                if (0 == json_object["data"]["attributes"]["total_votes"]["harmless"] and 
                    0 == json_object["data"]["attributes"]["total_votes"]["malicious"]):
                    msg+= "\n\n\t<span foreground='green' size='x-large'> OK - No viruses found</span>"
                    pref = "<span foreground='green'>"
                    suff = "</span>"
                else:
                    pref = "<span foreground='red'>"
                    suff = "</span>"
                    msg+= "\n\n\t<span foreground='red' size='x-large'> WARNING - Suspicious file !!!!</span>"

                json_formatted_str = "\tmd5sum: " +  json_object["data"]["attributes"]["md5"] + "\n"
                json_formatted_str += "\tharmless: " + pref + str(json_object["data"]["attributes"]["total_votes"]["harmless"]) + suff + "\n"
                json_formatted_str += "\tmalicious: " + pref + str(json_object["data"]["attributes"]["total_votes"]["malicious"]) + suff + "\n"

                #json_str = json.dumps(json_object, indent=2)
                #print(json_str)

            else:   
                msg+= "\n\n\t<span foreground='blue' size='x-large'>No info from VirusTotal</span>"
                json_formatted_str= ""

        elif 0 == file_stats.st_size:
                msg+= "\n\n\t<span foreground='blue' size='x-large'>Empty file - nothing to check</span>"
                json_formatted_str= ""        
        else:
                msg += """
                \n\n\t<span foreground='blue' size='x-large'>Set VirusTotal API Key variable</span>
                Obtain your key <a href='https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key'>here</a>        
                and add "export VIRUS_TOTAL_API_KEY=your_key" into your ~/.xsessionrc (you may need to restart your session)                 
                """
                json_formatted_str= ""

        
        msg+= "\n\n<small>"+json_formatted_str + "</small>"
        label.set_markup(msg)
        label.show()
        self.hbox.pack_start(label, False, False, 0)

        return Nautilus.PropertyPage(name="NautilusPython::virus_total",
                                     label=self.property_label, 
                                     page=self.hbox),
