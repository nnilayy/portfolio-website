# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import section dictionaries and timeline properties
from work_sections.blogs_dict import (
    blogs_data,
    blogs_timeline_colors,
    blogs_timeline_properties,
)
from work_sections.research_dict import (
    research_data,
    research_timeline_colors,
    research_timeline_properties,
)
from work_sections.internships_dict import (
    internships_data,
    internships_timeline_colors,
    internships_timeline_properties,
)
from work_sections.projects_dict import (
    projects_data,
    projects_timeline_colors,
    projects_timeline_properties,
)
from work_sections.extensions_dict import (
    extensions_data,
    extensions_timeline_colors,
    extensions_timeline_properties,
)
from work_sections.certifications_dict import (
    certifications_data,
    certifications_timeline_colors,
    certifications_timeline_properties,
)

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
sections = [
    "Blogs",
    "Research",
    "Internships",
    "Projects",
    "Extensions",
    "Certifications",
]

section_colors = {
    "Blogs": blogs_timeline_colors,
    "Research": research_timeline_colors,
    "Internships": internships_timeline_colors,
    "Projects": projects_timeline_colors,
    "Extensions": extensions_timeline_colors,
    "Certifications": certifications_timeline_colors,
}

# Data for timeline properties
section_timeline_properties = {
    "Blogs": blogs_timeline_properties,
    "Research": research_timeline_properties,
    "Internships": internships_timeline_properties,
    "Projects": projects_timeline_properties,
    "Extensions": extensions_timeline_properties,
    "Certifications": certifications_timeline_properties,
}

# Updated data structure with all sections
section_data = {
    "Blogs": blogs_data,
    "Research": research_data,
    "Internships": internships_data,
    "Projects": projects_data,
    "Extensions": extensions_data,
    "Certifications": certifications_data,
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


@app.get("/section_timeline_properties")
def get_section_timeline_properties():
    return section_timeline_properties


# If you want to get data for a specific section (combining data and colors)
@app.get("/section_info/{section_name}")
def get_section_info(section_name: str):
    if section_name in sections:
        section_entry = section_data.get(section_name, {})
        return {
            "section": section_name,
            "colors": section_colors.get(section_name, {}),
            "timelineProperties": section_timeline_properties.get(section_name, {}),
            "numCheckpoints": section_entry.get("numCheckpoints", 0),
            "checkpoints": section_entry.get("checkpoints", []),
        }
    else:
        raise HTTPException(status_code=404, detail="Section not found")
