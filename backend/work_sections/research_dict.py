# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
research_timeline_colors = {
    "timelineDarkPath": "#212120",
    "timelineBrightLine": "#007bff",
    "checkpointDefaultColor": "#212120",
    "checkpointPassedColor": "#d2d6fc",
    "checkpointGlowColor": "#8888FF",
    "boxShadow": "0 0 6px rgb(135, 155, 255)",
}
# -----------------------------------------------------------------------------
# CLASSES-DICT
# -----------------------------------------------------------------------------
research_classes_dict = {
    "outerClassName": "outer-content-research",
    "titleClassName": "content-page-title-research",
    "contentClassName": "content-page-content-research",
    "imgClassName": "content-image-research",
    "videoClassName": "content-page-video-research",
    "linkClassName": "",
}
# -----------------------------------------------------------------------------
# CONTENT-DATASTRUCTURE
# -----------------------------------------------------------------------------
temp_data = {
    "numCheckpoints": 4,
    "checkpoints": [
        {
            "checkpoint": 1,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Research Paper 1 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Research Paper 1 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
            ],
        },
        {
            "checkpoint": 2,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Research Paper 2 - Only Page",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                }
            ],
        },
        {
            "checkpoint": 3,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Research Paper 3 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Research Paper 3 - Page 2",
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
                    "title": "Research Paper 4 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Research Paper 4 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 3,
                    "title": "Research Paper 4 - Page 3",
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
    checkpoint["pages"] = [{**page, **research_classes_dict} for page in checkpoint["pages"]]

# Assign the final result to research_data
research_data = temp_data
