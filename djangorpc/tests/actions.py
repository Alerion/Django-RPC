from djangorpc import RpcRouter, Error, Msg


class MainApiClass(object):

    def hello(self, username, user):
        return Msg(u'Hello, %s' % username)


router = RpcRouter('tests:router', {
    'MainApi': MainApiClass(),
})
