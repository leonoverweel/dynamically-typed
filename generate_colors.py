import glob
import json

import extcolors
import tqdm


in_path = "website/themes/dt-com/static/images/header/"
out_path = "website/data/channels.json"
min_sum = 50 * 2

main_colors = {}
for img_path in tqdm.tqdm(glob.glob(in_path + "channel-*.png")):
    channel_id = img_path.removeprefix(in_path + "channel-").removesuffix(".png")
    colors, pixel_count = extcolors.extract_from_path(img_path)
    r, g, b = [(r, g, b) for (r, g, b), p in colors if r + b + g > min_sum][0]
    main_colors[channel_id] = f"rgb({r}, {g}, {b})"

with open(out_path, "w") as out_file:
    json.dump(main_colors, out_file, sort_keys=True, indent=4)
