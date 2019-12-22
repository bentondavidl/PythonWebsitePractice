from flask import Blueprint, render_template, request, redirect
from noteapp.note_utils import get_notes, create_note, get_note_by_id

bp = Blueprint(
    __name__,
    __name__, 
    template_folder='templates', 
    url_prefix='/notes'
)

@bp.route('/')
def list():
    return render_template('note_list.html', notes=get_notes())

@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        title = request.form.get('note_title')
        content = request.form.get('note_content')

        note = create_note(title=title, content=content)

        return redirect('/notes/view/' + note['id'])

    return render_template('note_edit.html')

@bp.route('/view/<note_id>')
def view(note_id):
    note = get_note_by_id(note_id)
    return render_template('note_view.html', note=note)