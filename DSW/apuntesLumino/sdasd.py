def edit_marks(request, subject-code: str):
    subject = subjectt.objects.get(code=subject-code)
    breadcrumb = Breadcrumbs()
    breadcrumb.add('My Subjects', reverse('my-subjects'))
    breadcrumbs.add(subject.code, reverse('subjects:subject-detail', args=[subject.code]))
