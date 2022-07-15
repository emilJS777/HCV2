from werkzeug.utils import redirect

from src import app
from src.__Parents.Controller import Controller
from flask import render_template, request

from src.Unit.UnitRepository import UnitRepository
from src.Sphere.SpeheRepository import SphereRepository
from src.Position.PositionRepository import PositionRepository
from src.IncomeType.IncomeTypeRepository import IncomeTypeRepository
from src.ExpenseType.ExpenseTypeRepository import ExpenseTypeRepository


class AdminController(Controller):
    unit_repository = UnitRepository()
    sphere_repository = SphereRepository()
    position_repository = PositionRepository()
    income_type_repository = IncomeTypeRepository()
    expense_type_repository = ExpenseTypeRepository()

    @staticmethod
    @app.route('/admin', methods=['GET'])
    def admin():
        units = AdminController.unit_repository.get_all()
        spheres = AdminController.sphere_repository.get_all()
        positions = AdminController.position_repository.get_all()
        income_types = AdminController.income_type_repository.get_all()
        expense_types = AdminController.expense_type_repository.get_all()
        return render_template('home.html',
                               units=units,
                               spheres=spheres,
                               positions=positions,
                               income_types=income_types,
                               expense_types=expense_types)

    # UNIT GET POST
    @staticmethod
    @app.route('/admin/unit', methods=['GET', 'POST'])
    def unit():
        if request.method == "POST":
            AdminController.unit_repository.create(body={'title': request.form['title'], 'description': request.form['description']})
            return redirect('/admin')

        return render_template('unit.html')

    # UNIT DELETE
    @staticmethod
    @app.route('/admin/unit/delete/<int:id>', methods=['GET'])
    def unit_delete(id):
        unit = AdminController.unit_repository.get_by_id(id)
        AdminController.unit_repository.delete(unit)
        return redirect('/admin')

    # SPHERE GET DELETE
    @staticmethod
    @app.route('/admin/sphere', methods=['GET', 'POST'])
    def sphere():
        if request.method == "POST":
            AdminController.sphere_repository.create(
                body={'name': request.form['name'], 'description': request.form['description']})
            return redirect('/admin')

        return render_template('sphere.html')

    # SPHERE DELETE
    @staticmethod
    @app.route('/admin/sphere/delete/<int:id>', methods=['GET'])
    def sphere_delete(id):
        sphere = AdminController.sphere_repository.get_by_id(id)
        AdminController.sphere_repository.delete(sphere)
        return redirect('/admin')

    # POSITION GET POST
    @staticmethod
    @app.route('/admin/position', methods=['GET', 'POST'])
    def position():
        if request.method == "POST":
            AdminController.position_repository.create(
                body={'title': request.form['title'], 'description': request.form['description']})
            return redirect('/admin')

        return render_template('position.html')

    # POSITION DELETE
    @staticmethod
    @app.route('/admin/position/delete/<int:id>', methods=['GET'])
    def position_delete(id):
        position = AdminController.position_repository.get_by_id(id)
        AdminController.position_repository.delete(position)
        return redirect('/admin')

    # INCOME GET POST
    @staticmethod
    @app.route('/admin/income_type', methods=['GET', 'POST'])
    def income_type():
        if request.method == "POST":
            AdminController.income_type_repository.create(
                body={'title': request.form['title'], 'description': request.form['description']})
            return redirect('/admin')

        return render_template('income_type.html')

    # INCOME DELETE
    @staticmethod
    @app.route('/admin/income_type/delete/<int:id>', methods=['GET'])
    def income_type_delete(id):
        income_type = AdminController.income_type_repository.get_by_id(id)
        AdminController.income_type_repository.delete(income_type)
        return redirect('/admin')

    # EXPENSE GET POST
    @staticmethod
    @app.route('/admin/expense_type', methods=['GET', 'POST'])
    def expense_type():
        if request.method == "POST":
            AdminController.expense_type_repository.create(
                body={'title': request.form['title'], 'description': request.form['description']})
            return redirect('/admin')

        return render_template('expense_type.html')

    # EXPENSE DELETE
    @staticmethod
    @app.route('/admin/expense_type/delete/<int:id>', methods=['GET'])
    def expense_type_delete(id):
        expense_type = AdminController.expense_type_repository.get_by_id(id)
        AdminController.expense_type_repository.delete(expense_type)
        return redirect('/admin')
