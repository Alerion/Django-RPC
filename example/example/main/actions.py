from djangorpc import RpcRouter, Error, Msg
from djangorpc.decorators import form_handler
from .forms import FeedbackForm


class MainApiClass(object):

    def hello(self, username, user):
        return Msg(u'Hello, %s' % username)

    def func1(self, val, d='default', *args, **kwargs):
        print 'val =', val
        print 'd =', d
        print 'args =', args
        print 'kwargs =', kwargs
        return Msg(u'func1')

    @form_handler
    def submit(self, rdata, user):
        form = FeedbackForm(rdata)
        if form.is_valid():
            form.send()
            return Msg(u'Thank you for feedback.')
        else:
            return Error(form.get_errors())


router = RpcRouter('main:router', {
    'MainApi': MainApiClass(),
})
