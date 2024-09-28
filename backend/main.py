# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

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
    },
    "Research": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#007bff",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#d2d6fc",
        "checkpointGlowColor": "#8888FF",
    },
    "Internships": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#0dfc00",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#dcf7dd",
        "checkpointGlowColor": "#88FF88",
    },
    "Projects": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#f8ff30",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#fbfcdc",
        "checkpointGlowColor": "#FFCC88",
    },
    "Extensions": {
        "timelineDarkPath": "#212120",
        "timelineBrightLine": "#7519ff",
        "checkpointDefaultColor": "#212120",
        "checkpointPassedColor": "#e5d4fc",
        "checkpointGlowColor": "#CC88FF",
    },
}

# Your data can be stored here or loaded from a file/database
section_data = {
    "Blogs": {
        "numCheckpoints": 3,
        "data": [
            {"content": ["Blog Post 1 - Page 1", "Blog Post 1 - Page 2"]},
            {"content": ["Blog Post 2 - Only Page"]},
            {"content": ["Blog Post 3 - Page 1", "Blog Post 3 - Page 2", "Blog Post 3 - Page 3"]},
        ],
    },
    "Research": {
        "numCheckpoints": 4,
        "data": [
            {"content": ["Research Paper 1 - Page 1", "Research Paper 1 - Page 2"]},
            {"content": ["Research Paper 2 - Only Page"]},
            {"content": ["Research Paper 3 - Page 1", "Research Paper 3 - Page 2"]},
            {"content": ["Research Paper 4 - Page 1", "Research Paper 4 - Page 2", "Research Paper 4 - Page 3"]},
        ],
    },
    "Internships": {
        "numCheckpoints": 5,
        "data": [
            {"content": ["Internship 1 - Page 1"]},
            {"content": ["Internship 2 - Page 1", "Internship 2 - Page 2"]},
            {"content": ["Internship 3 - Only Page"]},
            {"content": ["Internship 4 - Page 1", "Internship 4 - Page 2", "Internship 4 - Page 3"]},
            {"content": ["Internship 5 - Page 1", "Internship 5 - Page 2"]},
        ],
    },
    "Projects": {
        "numCheckpoints": 6,
        "data": [
            {"content": ["Project 1 - Only Page"]},
            {"content": ["Project 2 - Page 1", "Project 2 - Page 2"]},
            {"content": ["Project 3 - Page 1", "Project 3 - Page 2", "Project 3 - Page 3"]},
            {"content": ["Project 4 - Only Page"]},
            {"content": ["Project 5 - Page 1", "Project 5 - Page 2"]},
            {"content": ["Project 6 - Page 1", "Project 6 - Page 2"]},
        ],
    },
    "Extensions": {
        "numCheckpoints": 2,
        "data": [
            {"content": ["Extension 1 - Only Page"]},
            {"content": ["Extension 2 - Page 1", "Extension 2 - Page 2"]},
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
        return {
            "section": section_name,
            "colors": section_colors.get(section_name, {}),
            "data": section_data.get(section_name, {}),
        }
    else:
        raise HTTPException(status_code=404, detail="Section not found")

