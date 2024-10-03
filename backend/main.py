# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your data
sections = ['Blogs', 'Research', 'Internships', 'Projects', 'Extensions']

section_colors = {
    "Blogs": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#ff3030",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#f7e6e6",
        "checkpointGlowColor": "#FF8888",
        "boxShadow": "0 0 6px rgb(255, 91, 91)",
    },
    "Research": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#007bff",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#d2d6fc",
        "checkpointGlowColor": "#8888FF",
        "boxShadow": "0 0 6px rgb(135, 155, 255)",
    },
    "Internships": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#0dfc00",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#dcf7dd",
        "checkpointGlowColor": "#88FF88",
        "boxShadow": "0 0 6px rgb(169, 255, 179)",
    },
    "Projects": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#f8ff30",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#fbfcdc",
        "checkpointGlowColor": "#FFCC88",
        "boxShadow": "0 0 6px rgb(251, 255, 134)",
    },
    "Extensions": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#7519ff",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#e5d4fc",
        "checkpointGlowColor": "#CC88FF",
        "boxShadow": "0 0 6px rgb(170, 141, 255)",
    },
}

# Updated data structure with all sections
section_data = {
    "Blogs": {
        "numCheckpoints": 3,
        "checkpoints": [
            {
                "checkpoint": 1,
                "pages": [
                    {
                        "pageNumber": 1,
                        "title": "Blog Post 1 - Page-1",
                        "content": "You are an AI Assistant. You are an extremely kind and respectful assistant. Even in very harsh and disrespectful user prompts and queries, you are apologetic and are extremely regardful of the user's frustration and You try to solve the problem once more from a different point of view.",
                        "image": "Image",
                        "video": "Video",
                        "link": "www.google.com",
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Blog Post 1 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "link": "",
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Blog Post 3 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                    {
                        "pageNumber": 3,
                        "title": "Blog Post 3 - Page 3",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                ],
            },
        ],
    },
    "Research": {
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Research Paper 1 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Research Paper 3 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Research Paper 4 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                    {
                        "pageNumber": 3,
                        "title": "Research Paper 4 - Page 3",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                ],
            },
        ],
    },
    "Internships": {
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
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Internship 2 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Internship 4 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                    {
                        "pageNumber": 3,
                        "title": "Internship 4 - Page 3",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Internship 5 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                ],
            },
        ],
    },
    "Projects": {
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
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Project 2 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Project 3 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                    {
                        "pageNumber": 3,
                        "title": "Project 3 - Page 3",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Project 5 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Project 6 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                ],
            },
        ],
    },
    "Extensions": {
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
                        "className": "",
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
                        "className": "",
                    },
                    {
                        "pageNumber": 2,
                        "title": "Extension 2 - Page 2",
                        "content": "",
                        "image": "",
                        "video": "",
                        "link": "",
                        "className": "",
                    },
                ],
            },
        ],
    },
}

@app.get("/sections")
def get_sections():
    return sections

@app.get("/section_colors")
def get_section_colors():
    return section_colors

@app.get("/section_data")
def get_section_data():
    return section_data

# If you want to get data for a specific section (combining data and colors)
@app.get("/section_info/{section_name}")
def get_section_info(section_name: str):
    if section_name in sections:
        section_entry = section_data.get(section_name, {})
        return {
            "section": section_name,
            "colors": section_colors.get(section_name, {}),
            "numCheckpoints": section_entry.get("numCheckpoints", 0),
            "checkpoints": section_entry.get("checkpoints", []),
        }
    else:
        raise HTTPException(status_code=404, detail="Section not found")

