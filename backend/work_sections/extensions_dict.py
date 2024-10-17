# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
extensions_timeline_colors = {
    "timelineDarkPath": "#212120",
    "timelineBrightLine": "#7519ff",
    "checkpointDefaultColor": "#212120",
    "checkpointPassedColor": "#e5d4fc",
    "checkpointGlowColor": "#CC88FF",
    "boxShadow": "0 0 6px rgb(170, 141, 255)",
}
# -----------------------------------------------------------------------------
# CLASSES-DICT
# -----------------------------------------------------------------------------
extensions_classes_dict = {
    "outerClassName": "outer-content-blogs",
    "titleClassName": "content-page-title-blogs",
    "contentClassName": "content-page-content-blogs",
    "imgClassName": "content-image-blogs",
    "videoClassName": "content-page-video-blogs",
    "linkClassName": "",
}
# -----------------------------------------------------------------------------
# CONTENT-DATASTRUCTURE
# -----------------------------------------------------------------------------
temp_data = {
    "numCheckpoints": 2,
    "checkpoints": [
        {
            "checkpoint": 1,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Extension 1 - Only Page",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                }
            ],
        },
        {
            "checkpoint": 2,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Extension 2 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Extension 2 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
            ],
        },
    ],
}



# Add the class names to each page using a one-line for loop
for checkpoint in temp_data["checkpoints"]:
    checkpoint["pages"] = [{**page, **extensions_classes_dict} for page in checkpoint["pages"]]

# Assign the final result to extensions_data
extensions_data = temp_data
