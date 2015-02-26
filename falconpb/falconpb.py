"""Falcon hooks for (de)encoding http request/response to/from protobuf."""

import falcon
import json
import protobuf_to_dict


def require_json(req, resp, resource, params):
    """Falcon hook to require client to accept JSON.

    Raise HTTPNotAcceptable if client does not accept JSON.
    """
    if not req.client_accepts_json:
        raise falcon.HTTPNotAcceptable('HTTP client not accepting JSON.')


class ProtocolBuffersResource(object):
    """Protocol Buffers based resource."""

    def __init__(self, pb_class):
        """Init.

        :param pb_class: A protobuf class
        """
        self.pb_class = pb_class

        for http_method in falcon.HTTP_METHODS:
            if hasattr(pb_class, http_method):
                method = http_method.lower()
                setattr(self, 'on_%s' % method, self._on_prototype)

    @falcon.before(require_json)
    def _on_prototype(self, req, resp, **kwargs):
        """A prototype for method handlers (on_get(), etc)."""
        self._handle(req, resp, **kwargs)

    def _handle(self, req, resp, **kwargs):
        """Convert request data to protobuf and invoke appropriate handler."""
        pb = self._to_pb(req, kwargs)

        handle = getattr(self, 'handle_%s' % req.method.lower())
        result = handle(req, resp, pb, **kwargs)
        resp_dict = protobuf_to_dict.protobuf_to_dict(result)

        if resp_dict:
            resp.body = json.dumps(resp_dict)

    def _to_pb(self, req, url_params):
        """Return a protobuf given the request and the URL params."""
        body = req.stream.read() or '{}'

        try:
            body_dict = json.loads(body)
        except ValueError:
            raise falcon.HTTPBadRequest('Invalid request',
                                        'Cannot parse JSON in request body.')

        # Copy URL params and URL query params.
        for params in (url_params, req.params):
            for key in params:
                body_dict[key] = params[key]

        pb_class = getattr(self.pb_class, req.method)
        return protobuf_to_dict.dict_to_protobuf(pb_class, body_dict)
