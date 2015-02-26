"""Unit tests."""

import falcon
import falconpb

from falcon import testing

from tests import PingResource_pb2


class PingResource(falconpb.ProtocolBuffersResource):
    def __init__(self):
        super(PingResource, self).__init__(PingResource_pb2.PingResource)

        # Pointers to various objects for test assertion.
        self.req = None
        self.resp = None
        self.pb = None

        self.result = None

    def handle_get(self, req, resp, pb, greeting_from_url):
        self.req = req
        self.resp = resp
        self.pb = pb

        return pb.Response(reply='pong')

    def handle_post(self, req, resp, pb):
        self.req = req
        self.resp = resp
        self.pb = pb

        return pb.Response(reply='pong')


class ProtocolBuffersResourceTest(testing.TestBase):

    def before(self):
        self.resource = PingResource()
        self.api.add_route('/', self.resource)
        self.api.add_route('/{greeting_from_url}', self.resource)

    def test_get(self):
        self.simulate_request('/a111', query_string='greeting_from_query=a222')
        self.assertEqual(self.resource.resp.status, falcon.HTTP_200)
        self.assertEqual(self.resource.pb.greeting_from_url, 'a111')
        self.assertEqual(self.resource.pb.greeting_from_query, 'a222')
        self.assertEqual(self.resource.resp.body, '{"reply": "pong"}')

    def test_post(self):
        self.simulate_request('/', method='POST',
                              body='{"greeting": "ping"}')
        self.assertEqual(self.resource.resp.status, falcon.HTTP_200)
        self.assertEqual(self.resource.pb.greeting, 'ping')
        self.assertEqual(self.resource.resp.body, '{"reply": "pong"}')

    def test_bad_json_post(self):
        self.simulate_request('/', method='POST',
                              body='{"greet')
        self.assertEqual(self.srmock.status, falcon.HTTP_400)

    def test_no_json(self):
        headers = {
            'Accept': 'application/xml'
        }
        self.simulate_request('/a111', headers=headers)
        self.assertEqual(self.srmock.status, falcon.HTTP_406)
