import urllib
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import set_script_prefix
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template import RequestContext, loader, Context
from formtools.wizard.views import CookieWizardView
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
        form = forms.OpportunityListForm(request.GET)
        if form.is_valid():
            self.opportunities = form.cleaned_data['opportunities']
        else:
            raise Exception(
                "%s is an invalid set of opportunity ids." % request.GET)

        return super(ContactFormView, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        combined = {}
        for form in form_list:
            combined.update(form.cleaned_data)
        contact = models.Contact(**combined)
        contact.search = self.search
        contact.save()
        by_agency = {}
        for opp in self.opportunities:
            contact.opportunities.add(opp)
            agency = opp.agency
            by_agency.setdefault(agency, []).append(opp)
        set_script_prefix(settings.SITE_URL)
        for agency, opps in by_agency.items():
            tmp = loader.get_template('primerpeso/email.txt')
            body = tmp.render(Context({
                'contact': contact,
                'search': self.search,
                'agency': agency,
                'opportunities': opps,
            }))
            email = EmailMessage(
                _('Application Form PrimerPeso'),
                body,
                'noreply.primerpeso@cce.pr.gov',
                [agency.email, contact.email],
                [],
                reply_to=[agency.email, contact.email],
            )
            email.send()
        set_script_prefix('')
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
