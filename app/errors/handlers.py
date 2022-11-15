"""
Blueprint for error handling
"""
from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Implement handler for 404 error
    """
    return render_template('/errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    Implemenet handler for 500 error
    """
    db.session.rollback()
    return render_template('/errors/500.html'), 500