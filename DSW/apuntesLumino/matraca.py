from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from crispy_forms.bootstrap import FormActions

def __init__(self, subject, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper.layout = Layout(
        Field('title'),
        Field('content'),
        FormActions(
            Submit('Add', 'Add Lesson', css_class='mt-2 mb-2'),
            HTML(
                '<a class="btn btn-danger" href="{% subject.get_absolute_url %}">Cancel</a>'
            )
        )
    )



from django import template

register = template.Library()
@register.inclusion_tag('subjects/marks/mark.html')
def pretty_mark(mark: int | None):
    if mark is None:
        css_class = ''
        mark_value = '_'
    else:
        css_class = 'text-danger' if mark < 5 else 'text-success'
        mark_value = mark
    return dict(mark=mark_value, css_class=css_class)


@register.inclusion_tag('subjects/mark_student/label.html')
def student_label(formset, form_index):
    student = formset.forms[form_index].instance.student
    return dict(student=student)

# templatetags en plantilla
# <span class="{{ css_class }}">{{ mark }}</span>

# Plantilla de mark_list
# <td> {{% pretty_mark enrollment.mark %}}</td>
