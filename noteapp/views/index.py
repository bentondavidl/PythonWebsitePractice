from flask import Blueprint, redirect

bp = Blueprint(
    __name__,
    __name__, 
    template_folder='templates'
)

@bp.route('/')
def list():
    return redirect('/notes')
