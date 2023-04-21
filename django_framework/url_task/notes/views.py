from django.shortcuts import render
from .models import notes

def home(request):
    return render(request, 'notes/index.html')

def notes_sections(request):
    return render(request, 'notes/notes-section.html')

def browse_section(request, section_name):
    notes_list = []
    for note in notes:
        if note['section'] == section_name:
            notes_list.append(note['text'])
            
    return render(request, 'notes/notes.html', {"notes": notes_list, "section_name":section_name})

def notes_search(request, search_term):
    notes_list =[]
    for note in notes:
        # Search list to find a matching word 
        word_list = note['text'].split()
        if search_term in word_list:
            notes_list.append(note['text'])
            
    return render(request, 'notes/notes-search.html', {"notes": notes_list, "term": search_term})

def notes_by_num(request, note_id):
    note = notes[note_id - 1]
    return render(request, 'notes/notes_num.html', {"note": note, "note_id": note_id})
    
        
