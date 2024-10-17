# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
internships_timeline_colors = {
    "timelineDarkPath": "#212120",
    "timelineBrightLine": "#0dfc00",
    "checkpointDefaultColor": "#212120",
    "checkpointPassedColor": "#dcf7dd",
    "checkpointGlowColor": "#88FF88",
    "boxShadow": "0 0 6px rgb(169, 255, 179)",
}
# -----------------------------------------------------------------------------
# CLASSES-DICT
# -----------------------------------------------------------------------------
internships_classes_dict = {
    "outerClassName": "outer-content-internships",
    "titleClassName": "content-page-title-internships",
    "contentClassName": "content-page-content-internships",
    "imgClassName": "content-image-internships",
    "videoClassName": "content-page-video-internships",
    "linkClassName": "",
}
# -----------------------------------------------------------------------------
# CONTENT-DATASTRUCTURE
# -----------------------------------------------------------------------------
temp_data = {
    "numCheckpoints": 5,
    "checkpoints": [
        {
            "checkpoint": 1,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Internship 1 - Page 1",
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
                    "title": "Internship 2 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Internship 2 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
            ],
        },
        {
            "checkpoint": 3,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Internship 3 - Only Page",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                }
            ],
        },
        {
            "checkpoint": 4,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Internship 4 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Internship 4 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 3,
                    "title": "Internship 4 - Page 3",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
            ],
        },
        {
            "checkpoint": 5,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Internship 5 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Internship 5 - Page 2",
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
    checkpoint["pages"] = [{**page, **internships_classes_dict} for page in checkpoint["pages"]]

# Assign the final result to internships_data
internships_data = temp_data
