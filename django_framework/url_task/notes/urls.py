from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("sections/", views.notes_sections, name="notes-sections"),
    path("sections/<str:section_name>/", views.browse_section, name="browse-section"),
    path("<str:search_term>/", views.notes_search, name='notes-search'),
    path("<int:note_id>", views.notes_by_num, name="notes-by-num"),
]