# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
blogs_timeline_colors = {
    "timelineDarkPath": "#212120",
    "timelineBrightLine": "#ff3030",
    "checkpointDefaultColor": "#212120",
    "checkpointPassedColor": "#f7e6e6",
    "checkpointGlowColor": "#FF8888",
    "boxShadow": "0 0 6px rgb(255, 91, 91)",
}

# -----------------------------------------------------------------------------
# TIMELINE PROPERTIES
# -----------------------------------------------------------------------------
blogs_timeline_properties = {
    "lineLength": 1600,  # Customize as needed
    "lineWidth": 600,
    "amplitude": 200,
    "frequency": 400,
    "speed": 1.0,
}

# -----------------------------------------------------------------------------
# CLASSES-DICT
# -----------------------------------------------------------------------------
blogs_classes_dict = {
    "outerClassName": "outer-content-blogs",
    "titleClassName": "content-page-title-blogs",
    "contentClassName": "content-page-content-blogs",
    "imgClassName": "content-image-blogs",
    "videoClassName": "content-page-video-blogs",
    "linkClassName": "content-page-link-blogs",
}

# -----------------------------------------------------------------------------
# CONTENT-DATASTRUCTURE
# -----------------------------------------------------------------------------
temp_data = {
    "numCheckpoints": 3,
    "checkpoints": [
        {
            "checkpoint": 1,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Blog Post 1 - Page-1",
                    "content": "You are an AI Assistant. You are an extremely kind and respectful assistant. Even in very harsh and disrespectful user prompts and queries, you are apologetic and are extremely regardful of the user's frustration and You try to solve the problem once more from a different point of view.",
                    "image": "",
                    "video": "",
                    "link": "https://www.google.com/",
                },
                {
                    "pageNumber": 2,
                    "title": "Blog Post 1 - Page 2",
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
                    "title": "Blog Post 2 - Only Page",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "https://www.youtube.com/results?search_query=sidemen",
                }
            ],
        },
        {
            "checkpoint": 3,
            "pages": [
                {
                    "pageNumber": 1,
                    "title": "Blog Post 3 - Page 1",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "Blog Post 3 - Page 2",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 3,
                    "title": "Blog Post 3 - Page 3",
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
    checkpoint["pages"] = [
        {**page, **blogs_classes_dict} for page in checkpoint["pages"]
    ]

blogs_data = temp_data
