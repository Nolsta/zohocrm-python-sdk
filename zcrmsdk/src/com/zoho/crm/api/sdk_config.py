class SDKConfig(object):
    """
    The class to configure the SDK.
    """

    def __init__(self, auto_refresh_fields=False, pick_list_validation=True):
        """
        Creates an instance of SDKConfig with the following parameters

        Parameters:
            auto_refresh_fields(bool): A bool representing auto_refresh_fields
            pick_list_validation(bool): A bool representing pick_list_validation
        """
        self.__auto_refresh_fields = auto_refresh_fields
        self.__pick_list_validation = pick_list_validation

    def get_auto_refresh_fields(self):
        """
        This is a getter method to get auto_refresh_fields.

        Returns:
            bool: A bool representing auto_refresh_fields
        """
        return self.__auto_refresh_fields

    def get_pick_list_validation(self):
        """
        This is a getter method to get pick_list_validation.

        Returns:
            bool: A bool representing pick_list_validation
        """
        return self.__pick_list_validation
