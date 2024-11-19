"""
GetPostParametersMixin Mixin to handle GET and POST request parameters in Django views.
"""

from sharedlibrary.utils.request_session import (
    get_request_parameter_value,
    get_model_object_by_id,
    set_session_parameter_value,
    get_session_parameter_value
)


class GetPostParametersMixin(object):
    """
    Mixin to handle GET and POST request parameters in Django views. This mixin
    separates parameters between Model-based, LOCAL, SAVE, and switch types. It
    provides methods to load parameters from request and store them in session or
    other storage.
    """

    # Definitions of parameters for GET and POST requests
    get_parameters_definition = {}
    post_parameters_definition = {}

    # URL resolvers for GET parameters
    get_solvers_url = {}

    # Automatic saving of GET/POST parameters
    auto_save_get_parameters = True
    auto_save_post_parameters = True

    # Optional debugging
    print_save_method_results = False

    # Request object and parameter values
    request = None
    save_values = {}
    local_values = {}
    switch_values = {}

    def __init__(self, *args, **kwargs):
        """
        Initialize the mixin and update the parameters definition from child views.
        """
        # print("GetPostParametersMixin -> __init__")
        self.get_parameters_definition.update(self.set_additional_get_parameters())
        self.post_parameters_definition.update(self.set_additional_post_parameters())
        super().__init__(*args, **kwargs)

    def load_request_get_parameter_list(self, request):
        """
        Load and categorize GET parameters from the request. Parameters are sorted
        between SAVE, LOCAL, and switch categories, and then saved as needed.
        """
        self.request = request
        self.save_values = {}
        self.local_values = {}
        self.switch_values = {}
        self.clean_saved_get_parameters()

        if request.GET and any(x in self.request.GET.keys() for x in self.get_parameters_definition.keys()):
            for each in self.get_parameters_definition.keys():
                if self.get_parameters_definition[each] == "SAVE":
                    existuje_hodnota = get_request_parameter_value(self.request, 'GET', each)
                    if existuje_hodnota:
                        self.save_values[each] = existuje_hodnota
                elif self.get_parameters_definition[each] == "LOCAL":
                    existuje_hodnota = get_request_parameter_value(self.request, 'GET', each)
                    if existuje_hodnota:
                        self.local_values[each] = existuje_hodnota
                elif isinstance(self.get_parameters_definition[each], str):
                    existuje_hodnota = get_request_parameter_value(self.request, 'GET', each)
                    if existuje_hodnota == self.get_parameters_definition[each]:
                        self.switch_values[each] = existuje_hodnota
                else:
                    existuje_hodnota = get_request_parameter_value(self.request, 'GET', each)
                    if existuje_hodnota:
                        self.save_values[each] = get_model_object_by_id(self.get_parameters_definition[each], existuje_hodnota)

            if self.auto_save_get_parameters:
                self.save_get_parameters()

    def load_request_post_parameter_list(self, request):
        """
        Load and categorize POST parameters from the request. Parameters are sorted
        between SAVE, LOCAL, and switch categories, and then saved as needed.
        """
        self.request = request
        self.save_values = {}
        self.clean_saved_post_parameters()

        if request.POST and any(x in self.request.POST.keys() for x in self.post_parameters_definition.keys()):
            for each in self.post_parameters_definition.keys():
                if self.post_parameters_definition[each] == "SAVE":
                    existuje_hodnota = get_request_parameter_value(self.request, 'POST', each)
                    if existuje_hodnota:
                        self.save_values[each] = existuje_hodnota
                elif self.post_parameters_definition[each] == "LOCAL":
                    existuje_hodnota = get_request_parameter_value(self.request, 'POST', each)
                    if existuje_hodnota:
                        self.local_values[each] = existuje_hodnota
                elif isinstance(self.post_parameters_definition[each], str):
                    existuje_hodnota = get_request_parameter_value(self.request, 'POST', each)
                    if existuje_hodnota == self.post_parameters_definition[each]:
                        self.switch_values[each] = existuje_hodnota
                else:
                    existuje_hodnota = get_request_parameter_value(self.request, 'POST', each)
                    if existuje_hodnota:
                        self.save_values[each] = get_model_object_by_id(self.post_parameters_definition[each], existuje_hodnota)

            if self.auto_save_post_parameters:
                self.save_post_parameters()

    def save_get_parameters(self):
        """
        Save GET parameters to a storage method defined in child classes.
        """
        if self.print_save_method_results:
            self.print_save_values()

    def clean_saved_get_parameters(self):
        """
        Clean any saved GET parameters from previous requests to avoid inconsistencies.
        """
        pass

    def save_post_parameters(self):
        """
        Save POST parameters to a storage method defined in child classes.
        """
        if self.print_save_method_results:
            self.print_save_values()

    def clean_saved_post_parameters(self):
        """
        Clean any saved POST parameters from previous requests to avoid inconsistencies.
        """
        pass

    def set_additional_get_parameters(self):
        """
        Override this method in child views to add more GET parameters.
        """
        return self.get_parameters_definition

    def set_additional_post_parameters(self):
        """
        Override this method in child views to add more POST parameters.
        """
        return self.post_parameters_definition



"""
Extends GetPostParametersMixin to save and load GET/POST parameters into Django session
"""
from sharedlibrary.utils.request_session import (
    get_session_parameter_value,
    set_session_parameter_value,
    get_model_object_by_id
)
from sharedlibrary.mixins import GetPostParametersMixin


class SessionSaveGetParametersMixin(GetPostParametersMixin):
    """
    Mixin that extends GetPostParametersMixin to save and load GET/POST parameters
    into Django session. This mixin provides functionality to store parameters
    into session and retrieve them later.
    """

    def save_get_parameters(self):
        """
        Saves GET parameters into session. It checks whether the parameter is a
        model instance and stores its primary key or a simple value otherwise.
        """
        for each in self.save_values.keys():
            if self.get_parameters_definition[each] == "SAVE":
                set_session_parameter_value(self.request, each, self.save_values[each])
            else:
                model_instance_pk = self.save_values[each].pk if self.save_values[each] else None
                set_session_parameter_value(self.request, each, model_instance_pk)

    def clean_saved_get_parameters(self):
        """
        Cleans any previously saved GET parameters from the session to avoid
        inconsistencies. Deletes parameters from session based on the definition.
        """
        for each in self.get_parameters_definition.keys():
            delete = isinstance(self.get_parameters_definition[each], str) and self.get_parameters_definition[each] == 'SAVE'
            if delete:
                get_session_parameter_value(self.request, each, True)

    def reload_saved_get_parameters(self, clean_session=False):
        """
        Reloads previously saved GET parameters from session. If clean_session is
        True, the parameters are removed from session after being loaded.
        """
        for each in self.get_parameters_definition.keys():
            if self.get_parameters_definition[each] == "SAVE":
                self.save_values[each] = get_session_parameter_value(self.request, each, clean_session)
            else:
                self.save_values[each] = get_model_object_by_id(
                    self.get_parameters_definition[each],
                    get_session_parameter_value(self.request, each, clean_session)
                )


"""
Wrapper to automate addition of standard internal parameters to Django views

We usualy need  to wrap this mixin in some middle view or other middle mixin and define specific internal parameters
provided for views in three mixin components:

    - SessionSaveGetParametersMixin -> get_parameters_definition
                                    -> post_parameters_definition
    - InternalParametersMixin -> internal_parameters_names

Those three parametrs provide mechhanism to automatically set internal parametrs into View based on get/post names
and data type and then all child views based on this middle component will share same internal parameters...

Mixin is usefful for complex applications where we have many same repeated internal parametrs across many views...
"""
from sharedlibrary.mixins import SessionSaveGetParametersMixin, InternalParametersMixin


class DjangoPuzzleStandardViewParametersMixin(SessionSaveGetParametersMixin, InternalParametersMixin):
    """
    Mixin that provides automation for handling GET and POST parameters,
    including the dynamic assignment of internal variables.

    This mixin combines functionality from SessionSaveGetParametersMixin
    and InternalParametersMixin to streamline parameter handling and internal
    variable management in Django views.
    """

    def dispatch(self, request, *args, **kwargs):
        """
        Dispatch method that automatically processes GET and POST parameters
        and dynamically assigns internal variables before any child view logic.

        It ensures that parameters from the request are handled and
        internal parameters are set according to the definitions in
        `internal_parameters_names`.

        :param request: The HttpRequest object containing request data.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The result of the parent dispatch method.
        """
        # Process GET or POST parameters
        if request.method == "GET":
            self.load_request_get_parameter_list(request)
        elif request.method == "POST":
            self.load_request_post_parameter_list(request)

        # Dynamically assign internal parameters based on internal_parameters_names
        self.assign_internal_params()

        # Continue with the standard dispatch process
        return super().dispatch(request, *args, **kwargs)


class AsbdStandardViewParametersMixin(DjangoPuzzleStandardViewParametersMixin):
    """Startovni uroven definice GET, POST a INTERNICH parametru"""
    get_parameters_definition = {
        REQUEST_REFFERAL_DUM_GET_PARAMETER: Domy,
        REQUEST_REFFERAL_BYT_GET_PARAMETER: Byty,
        REQUEST_REFFERAL_SLUZBA_GET_PARAMETER: SluzbyDefinice,
    }

    post_parameters_definition = {
        REQUEST_REFFERAL_DUM_POST_PARAMETER: Domy,
        REQUEST_REFFERAL_BYT_POST_PARAMETER: Byty,
        REQUEST_REFFERAL_SLUZBA_POST_PARAMETER: SluzbyDefinice,
    }

    internal_parameters_names = {
        "referral_dum": REQUEST_REFFERAL_DUM_GET_PARAMETER,
        "referral_byt": REQUEST_REFFERAL_BYT_GET_PARAMETER,
        "referral_sluzba": REQUEST_REFFERAL_SLUZBA_GET_PARAMETER,
    }


class MeridlaViewParametersMixin(AsbdStandardViewParametersMixin):
    def set_additional_internal_parameters(self):
        aditional_parameters = super().set_additional_internal_parameters()
        aditional_parameters.update({
            "referral_meridlo": REQUEST_REFFERAL_MERIDLO_GET_PARAMETER,
        })
        return aditional_parameters

    def set_additional_get_parameters(self):
        aditional_parameters = super().set_additional_get_parameters()
        aditional_parameters.update({
            REQUEST_REFFERAL_MERIDLO_GET_PARAMETER: Meridla,
        })
        return aditional_parameters


class PokusParametry(LoginRequiredMixin,
                     DjangoPuzzleMixinWrapper,
                     MeridlaViewParametersMixin,
                     TemplateView):
    template_name = "pokusy_parametry.html"

    def set_additional_get_parameters(self):
        aditional_parameters = super().set_additional_get_parameters()
        aditional_parameters.update({
            "homer_simpson": "LOCAL",
        })
        return aditional_parameters

    def get(self, request, *args, **kwargs):
        """Just to print internal parameters"""
        self.print_internal_params()
        # Zpracujeme interní parametry (již bylo zajištěno v dispatch)
        return super().get(request, *args, **kwargs)

