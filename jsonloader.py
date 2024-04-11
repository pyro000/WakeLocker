import json
import os

def load():
  global hotkeys
  with open('settings.json') as f:
    hotkeys = json.load(f)
  return hotkeys

hotkeys = {
  "window": "EscapeFromTarkov",
  "hotkeys":[
    ["E", "j"],
    ["Q", "j"],
    ["Ctrl+p", "enabled"],
    ["Ctrl+o", "reload"]
  ]
}

if not os.path.exists("settings.json"):
  with open('settings.json', "w") as f:
    json.dump(hotkeys, f, indent=1)

load();