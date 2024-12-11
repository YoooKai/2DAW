# Importaciones necesarias
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.forms import forms, modelformset_factory
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, Submit, HTML
from crispy_forms.bootstrap import FormActions
from django import template
from .models import Subject, Enrollment  # Asegúrate de importar tus modelos correctamente

# Registro para los filtros de plantilla
register = template.Library()

# Función de vista para editar las calificaciones
def edit_marks(request, subject_code: str):
    # Obtener el objeto Subject o devolver 404 si no existe
    subject = get_object_or_404(Subject, code=subject_code)
    
    # Configurar el breadcrumb
    breadcrumbs = Breadcrumbs()
    breadcrumbs.add('My Subjects', reverse('my-subjects'))
    breadcrumbs.add(subject.code, reverse('subjects:subject-detail', args=[subject.code]))
    
    # Obtener los enrollments relacionados con el subject
    enrollments = Enrollment.objects.filter(subject=subject)
    
    # Crear un formset de EditMarkForm
    EditMarkFormSet = modelformset_factory(Enrollment, form=EditMarkForm, extra=0)
    
    if request.method == 'POST':
        formset = EditMarkFormSet(request.POST, queryset=enrollments)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Las calificaciones se han actualizado correctamente.')
            return redirect(reverse('subjects:subject-detail', args=[subject.code]))
    else:
        formset = EditMarkFormSet(queryset=enrollments)
    
    # Configurar el helper de Crispy Forms
    formset_helper = EditMarkFormSetHelper()
    
    context = {
        'breadcrumbs': breadcrumbs,
        'subject': subject,
        'formset': formset,
        'formset_helper': formset_helper,
    }
    
    return render(request, 'subjects/edit_marks.html', context)

# Formulario para editar la calificación
class EditMarkForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['mark']

# Helper para el FormSet utilizando Crispy Forms
class EditMarkFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_show_labels = False
        self.layout = Layout(
            Row(
                HTML(
                    '{% load subject_extras %}<div class="col-md-2">{% student_label formset forloop.counter0 %}</div>'
                ),
                Field('mark', wrapper_class='col-md-2'),
                css_class='align-items-center'
            ),
            FormActions(
                Submit('save', 'Save Marks', css_class='mt-3'),
                HTML(
                    '<a class="btn btn-danger" href="{% url \'subjects:subject-detail\' subject.code %}">Cancel</a>'
                )
            )
        )

# Filtro personalizado para obtener las calificaciones de un estudiante
@register.filter
def get_marks(student, subject):
    try:
        enrollment = Enrollment.objects.get(student=student, subject=subject)
        return enrollment.mark if enrollment.mark is not None else '_'
    except Enrollment.DoesNotExist:
        return '_'
