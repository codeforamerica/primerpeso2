import urllib
from django.shortcuts import render, redirect
from formtools.wizard.views import CookieWizardView
from django.views.generic.detail import DetailView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from . import models, forms


def about(request):
    return render(request, "primerpeso/about.jade", {'title': _('About')})


def home(request):
    return render(request, "primerpeso/home.jade", {'title': _('Home')})


def thanks(request):
    return render(request, "primerpeso/thanks.jade",
                  {'title': _('Sent Email Confirmation')})


class SearchFormView(CookieWizardView):
    template_name = "primerpeso/search_form.html"

    def done(self, form_list, **kwargs):
        combined = {}
        for form in form_list:
            combined.update(form.cleaned_data)
        search = models.OpportunitySearch(**combined)
        search.save()
        url = reverse('search-results', args=[search.pk, ])
        return redirect(url)


class ContactFormView(CookieWizardView):
    template_name = "primerpeso/contact_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.search = get_object_or_404(models.OpportunitySearch, pk=args[0])
        return super(ContactFormView, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        combined = {}
        for form in form_list:
            combined.update(form.cleaned_data)
        contact = models.Contact(**combined)
        contact.search = self.search
        contact.save()
        url = reverse('thanks')
        return redirect(url)


def search_results(request, pk):
    try:
        search = models.OpportunitySearch.objects.get(pk=pk)
    except models.OpportunitySearch.DoesNotExist:
        return redirect(reverse('search-form'))
    if request.POST:
        form = forms.OpportunityListForm(request.POST)
        if form.is_valid():
            qs = request.POST.copy()
            del qs['csrfmiddlewaretoken']
            url = '%s?%s' % (reverse('contact-form', args=[search.pk, ]),
                    qs.urlencode())
            return redirect(url)
    segmented_opps = list(search.segment_search().items())
    return render_to_response("primerpeso/search_results.html", {
        'title': _('Questionnaire Results'),  # Preguntas
        'segmented_opps': segmented_opps,
    }, context_instance=RequestContext(request))


class OpportunityDetailView(DetailView):
    model = models.Opportunity
