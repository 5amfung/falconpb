# FalconPB

Protocol Buffers based resource for Falcon.


## How to install

```pip install falconpb```


## How to use

The base class encodes the URL parameters, query parameters, and the body
to a protobuf of your choice.  You have to define the protobuf.  The protobuf
message needs to have a message type with name that is the method name in
all caps.  With it, there should also be a message type called Response, which
is used for the HTTP response.

For example, subclass ```ProtocolBuffersResource``` and implement
the ```handle_get``` method.  Replace ```get``` with other http methods
for other type of methods.

The protobuf would look something like this:

    message GreetingPbResource {
        message GET {
            required string name = 1;
            optional string greeting = 2;
             
            message Response {
                optional string reply = 1;
        }
    }
 
 
The Falcon resource class would look something like this:

    from falconpb import ProtocolBuffersResource
    
    class GreetingResource(ProtocolBuffersResource):
        def __init__(self):
            super(GreetingResource, self).__init__(GreetingPbResource)
        
        def handle_get(self, res, req, pb, name):
            # Fill in your code here.
            whatever = pb.greeting
        
            # Return your response.
            return pb.Response(reply='Hi %s' % name)

    app = falcon.API()
    app.add_route('/{name}', GreetingResource())
