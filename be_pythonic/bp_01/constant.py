'''
Best practice 01

Put all constants in one file, and protect them from changing value.

'''


class Const(object):
    class ConstError(TypeError):
        pass
    
    class ConstCaseError(ConstError):
        pass
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value

const = Const()

const.MY_CONSTANT = "SAMPLE_STRING_01"
const.MY_SECOND_CONSTANT = "SAMPLE_STRING_02"

