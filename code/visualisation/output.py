# Armand Stiens, Willem Folkers, Dionne Ruigrok

import json 
import main
from code.classes import district, house, battery


def make_json(district, filename, current_district):
        """
        TODO
        """
        jsonfile = [{"district": int(current_district),
        "costs-own": district.cost_shared}
        ]

        batteries = district.batteries
        for battery in batteries:
                houses = []
                for house in batteries.get(battery).houses:
                        houses.append({"id": house.id,
                        "location": f"{house.x_cor},{house.y_cor}",
                        "output": house.output,
                        "cables": house.cables
                        })
                jsonfile.append({"id": batteries.get(battery).id,
                "location": f"{batteries.get(battery).x_cor},{batteries.get(battery).y_cor}",
                "capacity": batteries.get(battery).max_cap,
                "houses": houses
                })

        with open(filename, "w") as fp:
                json.dump(jsonfile, fp, indent=4)

        with open("results/output.json", "w") as fp:
                json.dump(jsonfile, fp, indent=4)
