from pprint import pprint

fab_data = {
  "fabLocation": "Fab 28, Kiryat Gat, Israel",
  "timestamp": "2024-07-02T08:52:00Z",
  "equipment": {
    "EUV_Lithography_01": {
      "status": "operational",
      "uptime": 98.5,
      "lastMaintenance": "2024-06-25",
      "alerts": []
    },
    "Etch_Tool_03": {
      "status": "maintenance",
      "uptime": 95.2,
      "lastMaintenance": "2024-06-30",
      "alerts": [
        "Temperature fluctuation exceeded threshold on 2024-06-28"
      ]
    },
    "CMP_Machine_12": {
      "status": "idle",
      "uptime": 97.8,
      "lastMaintenance": "2024-06-20",
      "alerts": []
    }
  },
  "yieldData": {
    "product": "Core i9-15900K",
    "lotID": "240701A",
    "wafers": 25,
    "passRate": 92.4,
    "defects": {
      "particleContamination": 12,
      "thinGateOxide": 5,
      "misalignment": 3
    }
  },
  "maintenanceSchedule": [
    {
      "equipment": "EUV_Lithography_01",
      "date": "2024-07-15",
      "type": "preventive",
      "description": "Laser source alignment and chamber cleaning"
    },
    {
      "equipment": "Etch_Tool_03",
      "date": "2024-07-05",
      "type": "corrective",
      "description": "Replace faulty RF generator"
    }
  ]
}

# print the date of last maintenance schedule ("2024-07-05")
# print particleContamination from defects from yield data (12)
# print all the alerts for Etch_Tool_03 ()
# update all the descriptions in maintenanceSchedule to upper case

for elem in fab_data["maintenanceSchedule"]:
  elem["description"] = elem["description"].upper()

pprint(fab_data)