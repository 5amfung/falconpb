"""Unit tests."""

import falcon
from falcon import testing

import falconpb
from tests import FooResource_pb2


class TestResource(falconpb.ProtocolBuffersResource):
    def __init__(self):
        super(TestResource, self).__init__(FooResource_pb2.FooResource)

        # Pointers to various objects for test assertion.
        self.req = None
        self.pb = None

        self.result = None

    def handle_get(self, req, resp, pb):
        self.req = req
        self.pb = pb

        self.result = pb.Response()
        self.result.greeting = 'Hello'

        return self.result

    def handle_post(self, req, resp, pb):
        self.req = req
        self.pb = pb

        self.result = pb.Response()
        self.result.id = 'abc123'

        return self.result


class ProtocolBuffersResourceTest(testing.TestBase):

    def before(self):
        self.resource = TestResource()
        self.api.add_route(self.test_route, self.resource)
        pass

    def test_post(self):
        self.simulate_request(self.test_route, method='POST',
                              body='{"greeting": "hello"}')
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.assertEqual(self.resource.pb.greeting, 'hello')
        self.assertEqual(self.resource.result.id, 'abc123')

    def test_bad_json_post(self):
        self.simulate_request(self.test_route, method='POST',
                              body='{"greet')
        self.assertEqual(self.srmock.status, falcon.HTTP_400)
