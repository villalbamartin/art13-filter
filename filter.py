#!/usr/bin/python3


class Filter:
    """ Class that implements an upload filter.

    """

    uncertain_string = ('the server doesn\'t know for sure whether this '
                        'file infringes copyright or not')

    def __init__(self):
        self.full_license = []
        self.whitelist = dict()

    def query(self, file):
        """Given a file, returns whether the file can be safely uploaded.

        Parameters
        ----------
        file : data
            The binary contents of the file.

        Returns
        -------
        dict
            A dictionary containing a return code 'code' and a human-readable
            explanation 'desc'.

        """
        retval = {'code': 403, 'desc': 'Forbidden: ' + self.uncertain_string}
        return retval
