# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
projects_timeline_colors = {
    "timelineDarkPath": "#212120",
    "timelineBrightLine": "#f8ff30",
    "checkpointDefaultColor": "#212120",
    "checkpointPassedColor": "#fbfcdc",
    "checkpointGlowColor": "#FFCC88",
    "boxShadow": "0 0 6px rgb(251, 255, 134)",
}
# -----------------------------------------------------------------------------
# CLASSES-DICT
# -----------------------------------------------------------------------------
projects_classes_dict = {
    "outerClassName": "outer-content-project",
    "titleClassName": "content-page-title-project",
    "contentClassName": "content-page-content-project",
    "imgClassName": "content-image-project",
    "videoClassName": "content-page-video-project",
    "linkClassName": "",
}
# -----------------------------------------------------------------------------
# CONTENT-DATASTRUCTURE
# -----------------------------------------------------------------------------
temp_data = {
    "numCheckpoints": 6,
    "checkpoints": [
        {
            "checkpoint": 1,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Project 1 - Only Page",
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
                    "title": "Project 2 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Project 2 - Page 2",
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
                    "title": "Project 3 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Project 3 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 3,
                    "title": "Project 3 - Page 3",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
            ],
        },
        {
            "checkpoint": 4,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Project 4 - Only Page",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                }
            ],
        },
        {
            "checkpoint": 5,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Project 5 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Project 5 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
            ],
        },
        {
            "checkpoint": 6,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Project 6 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Project 6 - Page 2",
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
    checkpoint["pages"] = [{**page, **projects_classes_dict} for page in checkpoint["pages"]]

# Assign the final result to projects_data
projects_data = temp_data
