# -----------------------------------------------------------------------------
# CERTIFICATIONS-IMAGES
# -----------------------------------------------------------------------------
certfication_1_image = "./Generative-AI-With-LLM.png"
certfication_2_image = "./Generative-AI-With-LLM.png"
certfication_3_image = "./Generative-AI-With-LLM.png"
certfication_4_image = "./Generative-AI-With-LLM.png"
certfication_5_image = "./Generative-AI-With-LLM.png"
certfication_6_image = "./Generative-AI-With-LLM.png"

# -----------------------------------------------------------------------------
# CERTIFICATIONS-NAMES
# -----------------------------------------------------------------------------
certification_1_name = "Generative AI with Large Language Models"
certification_2_name = "Generative AI with Large Language Models"
certification_3_name = "Generative AI with Large Language Models"
certification_4_name = "Generative AI with Large Language Models"
certification_5_name = "Generative AI with Large Language Models"
certification_6_name = "Generative AI with Large Language Models"

# -----------------------------------------------------------------------------
# CONTENT-TIMELINE-CSS
# -----------------------------------------------------------------------------
certifications_timeline_colors = {
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
classes_dict = {
    "outerClassName": "outer-content-certfications",
    "titleClassName": "content-page-title-certfications",
    "contentClassName": "content-page-content-certfications",
    "imgClassName": "content-image-certfications",
    "videoClassName": "content-page-video-certfications",
    "linkClassName": "hey",
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
                    "title": "",
                    "content": certification_1_name,
                    "image": certfication_1_image,
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
                    "title": "",
                    "content": certification_2_name,
                    "image": certfication_2_image,
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "",
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
                    "title": "",
                    "content": certification_3_name,
                    "image": certfication_3_image,
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
                    "title": "",
                    "content": certification_4_name,
                    "image": certfication_4_image,
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "",
                    "content": "",
                    "image": "",
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 3,
                    "title": "",
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
                    "title": "",
                    "content": certification_5_name,
                    "image": certfication_5_image,
                    "video": "",
                    "link": "",
                },
                {
                    "pageNumber": 2,
                    "title": "",
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
    checkpoint["pages"] = [{**page, **classes_dict} for page in checkpoint["pages"]]

# Assign the result to certifications_data
certifications_data = temp_data
