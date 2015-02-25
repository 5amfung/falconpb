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
        self.resp = None
        self.pb = None

        self.result = None

    def handle_get(self, req, resp, pb, id):
        self.req = req
        self.resp = resp
        self.pb = pb

        return pb.Response(greeting='Hello')

    def handle_post(self, req, resp, pb):
        self.req = req
        self.resp = resp
        self.pb = pb

        return pb.Response(id='abc123')


class ProtocolBuffersResourceTest(testing.TestBase):

    def before(self):
        self.resource = TestResource()
        self.api.add_route('/', self.resource)
        self.api.add_route('/{id}', self.resource)

    def test_get(self):
        self.simulate_request('/abc123')
        self.assertEqual(self.resource.resp.status, falcon.HTTP_200)
        self.assertEqual(self.resource.pb.id, 'abc123')
        self.assertEqual(self.resource.resp.body, '{"greeting": "Hello"}')

    def test_post(self):
        self.simulate_request('/', method='POST',
                              body='{"greeting": "hello"}')
        self.assertEqual(self.resource.resp.status, falcon.HTTP_200)
        self.assertEqual(self.resource.pb.greeting, 'hello')
        self.assertEqual(self.resource.resp.body, '{"id": "abc123"}')

    def test_bad_json_post(self):
        self.simulate_request('/', method='POST',
                              body='{"greet')
        self.assertEqual(self.srmock.status, falcon.HTTP_400)

