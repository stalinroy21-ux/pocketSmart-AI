from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from gemini_utils import generate_recommendation


app = FastAPI()

templates = Jinja2Templates(directory="templates")


# ==============================
# HOME PAGE
# ==============================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


# ==============================
# HOME INTERIOR
# ==============================

@app.post("/generate-home", response_class=HTMLResponse)
async def generate_home(
    request: Request,
    budget: float = Form(...),
    room: str = Form(...),
    items: str = Form(...)
):

    prompt = f"""
You are PocketSmart AI.

Create a Home Interior Budget Plan.

Budget: ₹{budget}

Room: {room}

Required Items:
{items}

Give suitable recommendations.

Include:
Item name
Estimated price
Quantity
Total price
Remaining budget

Keep the recommendation within the given budget.
"""

    result = generate_recommendation(prompt)

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "request": request,
            "result": result
        }
    )


# ==============================
# PARTY PLANNER
# ==============================

@app.post("/generate-party", response_class=HTMLResponse)
async def generate_party(
    request: Request,
    budget: float = Form(...),
    guests: int = Form(...),
    event: str = Form(...)
):

    prompt = f"""
You are PocketSmart AI.

Create a Party Budget Plan.

Budget: ₹{budget}

Guests: {guests}

Event Type: {event}

Divide the budget into:

Food
Decoration
Entertainment
Venue

Give practical recommendations within the budget.
"""

    result = generate_recommendation(prompt)

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "request": request,
            "result": result
        }
    )


# ==============================
# JEWELRY PLANNER
# ==============================

@app.post("/generate-jewelry", response_class=HTMLResponse)
async def generate_jewelry(
    request: Request,
    budget: float = Form(...),
    occasion: str = Form(...),
    style: str = Form(...)
):

    prompt = f"""
You are PocketSmart AI.

Create a Jewelry Budget Recommendation.

Budget: ₹{budget}

Occasion: {occasion}

Style: {style}

Recommend suitable jewelry within the budget.

Give:

Jewelry type
Suggested design
Estimated price
Reason
Remaining budget
"""

    result = generate_recommendation(prompt)

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "request": request,
            "result": result
        }
    )