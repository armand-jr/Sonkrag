import json 
import main
from code.classes import district, house, battery


def make_json(district, filename, current_district):
        jsonfile = [{"district": int(current_district),
        "costs-shared": district.cost_shared}
        ]
        batteries = district.batteries
        for battery in batteries:
                houses = []
                for house in batteries.get(battery).houses:
                        houses.append({"location": f"{house.x_cor},{house.y_cor}",
                        "output": house.output,
                        "cables": house.cables
                        })
                jsonfile.append({"location": f"{batteries.get(battery).x_cor},{batteries.get(battery).x_cor}",
                        "capacity": batteries.get(battery).max_cap,
                        "houses": houses
                })

        with open(filename, "w") as fp:
                json.dump(jsonfile, fp, indent=4, sort_keys=True)

