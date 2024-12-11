from django.shortcuts import get_object_or_404
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, HTML, Submit
from django import forms
from .models import Subject, Enrollment
from .utils import Breadcrumbs  # Asegúrate de que Breadcrumbs esté correctamente definido e importado
from django.template import Library

register = Library()

def edit_marks(request, subject_code: str):
    subject = get_object_or_404(Subject, code=subject_code)
    breadcrumbs = Breadcrumbs()
    breadcrumbs.add('My Subjects', reverse('my-subjects'))
    breadcrumbs.add(subject.code, reverse('subjects:subject-detail', args=[subject.code]))
    # Aquí puedes añadir lógica adicional según lo que haga tu vista


class EditMarkForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['mark']


class EditMarkFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_show_labels = False
        self.layout = Layout(
            Row(
                HTML(
                    '{% load subject_extras %}'
                    '<div class="col-md-2">'
                    '{% student_label formset forloop.counter0 %}'
                    '</div>'
                ),
                Field('mark', wrapper_class='col-md-2'),
                css_class='align-items-center'
            )
        )
        self.add_input(Submit('save', 'Save Marks', css_class='mt-3'))


@register.filter
def get_marks(student, subject):
    """
    Obtiene la calificación de un estudiante en una materia.
    """
    try:
        return student.enrollment_set.get(subject=subject).mark
    except Enrollment.DoesNotExist:
        return None
