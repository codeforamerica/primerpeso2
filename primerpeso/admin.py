from django.contrib import admin
from primerpeso import models, forms


class AddCreatorMixin:
    """Mixin which adds the user to the creator field.
    """

    def get_form(self, request, *args, **kwargs):
        form = super(AddCreatorMixin, self).get_form(request, *args, **kwargs)
        form.base_fields['creator'].initial = request.user
        return form


class AddCreator(AddCreatorMixin, admin.ModelAdmin):
    pass


class AddCreatorInline(admin.StackedInline, AddCreatorMixin):
    pass


class RequirementInlineAdmin(AddCreatorInline):
    form = forms.RequirementForm
    model = models.Requirement


class RequirementRelationshipAdmin(AddCreatorInline):
    form = forms.RequirementRelationshipForm
    model = models.RequirementRelationship
    extra = 1
    inlines = (RequirementInlineAdmin, )


@admin.register(models.Opportunity)
class OpportunityAdmin(AddCreator):
    readonly_fields = ('created_at', 'updated_at',)
    form = forms.OpportunityForm
    inlines = (RequirementRelationshipAdmin, )


@admin.register(models.Requirement)
class RequirementAdmin(AddCreator):
    readonly_fields = ('created_at', 'updated_at',)
    form = forms.RequirementForm


@admin.register(models.OpportunitySearch)
class OpportunitySearchAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('pk', 'created_at',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(OpportunitySearchAdmin,
                     self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('email', 'created_at',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(ContactAdmin,
                     self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Agency)
class AgencyAdmin(AddCreator):
    readonly_fields = ('created_at', 'updated_at',)
    form = forms.AgencyForm
    list_display = ('name', 'email', 'web',)
