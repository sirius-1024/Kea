import sys
sys.path.append("..")
from kea.main import *

class Test(Kea):
    

    @initialize()
    def set_up(self):
        d(resourceId="it.feio.android.omninotes:id/next").click()
        
        d(resourceId="it.feio.android.omninotes:id/next").click()
        
        d(resourceId="it.feio.android.omninotes:id/next").click()
        
        d(resourceId="it.feio.android.omninotes:id/next").click()
        
        d(resourceId="it.feio.android.omninotes:id/next").click()
        
        d(resourceId="it.feio.android.omninotes:id/done").click()
        
        if d(text="OK").exists():
            d(text="OK").click()
            
    @main_path()
    def check_languge_selection_mainpath(self):
        d(description="drawer open").click()
        d(text="SETTINGS").click()
        d(text="Interface").click()
    
    @precondition(lambda self: d(text="Interface").exists() and d(text="Language").exists())
    @rule()
    def check_languge_selection(self):
        
        d(text="Language").click()
        
        assert d(scrollable=True).scroll.to(text="Suomi (Finnish)"), "Finnish"
   


t = Test()

setting = Setting(
    apk_path="./apk/omninotes/OmniNotes-5.4.5.apk",
    device_serial="emulator-5554",
    output_dir="../output/omninotes/674/mutate",
    policy_name="mutate"
)
start_kea(t,setting)

