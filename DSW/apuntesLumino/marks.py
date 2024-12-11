from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.forms.models import modelformset_factory
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, HTML, Submit
from django import forms
from .models import Subject, Enrollment
from .utils import Breadcrumbs
from django.template import Library

register = Library()

def edit_marks(request, subject_code: str):
    subject = subjects.objects.get(code=subject_code)
    breadcrumbs = Breadcrumbs()
    breadcrumbs.add('My Subjects', reverse('my-subjects'))
    breadcrumbs.add(subject.code, reverse('subjects:subject-detail', args=[subject.code]))
    
    MarkFormset = modelformset_factory(Enrollment, form=EditMarkForm, extra=0)
    queryset = subject.enrollments.all()

    if request.method == 'POST':
        formset = MarkFormset(queryset=queryset, data=request.POST)
        if formset.is_valid():
            formset.save()
            messages.add_message(request, messages.SUCCESS, 'Marks Successfully Saved')
            return redirect(reverse('subjects:edit_marks', kwargs={'subject_code': subject_code}))
    else:
        formset = MarkFormset(queryset=queryset)

    helper = EditMarkFormSetHelper()
    return render(
        request,
        'subjects/marks/edit_marks.html',
        {
            'subject': subject,
            'formset': formset,
            'helper': helper,
            'breadcrumbs': breadcrumbs
        }
    )


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


