Complete the Dockerfile in the server directory to define a new server
image.

Complete the Dockerfile in the client directory to define a new client
image.

Your server and client images will be built using the script "run.sh" in
this directory.

When the client is run, it must output the message:

  "Nobody expects the Spanish Inquisition!"

The details of the format of the output do not matter.  It could be a
textual message as above, or the words could either the rows or the
columns of a database table written to standard output.

What matters is that the words are fetched by the client from the server.

These words *must not* be embedded within the client at all.

One obvious and relatively straightforward way of achieving this is by
having the server run httpd, and having the client use "wget" to fetch
the message from the server.

The marks for this approach (or similar) will be capped at 60%.

I am imagining that some alternative approaches may be more ambitious than
others.  For example, an approach involving a redis server would be only
slightly more ambitious than the HTTP approach, whereas one in which the
client uses SSH to access the server would be substantially more ambitious.

Higher marks will be awarded for more ambitious solutions.

For the client, you should use the ENTRYPOINT directive to set the program
which runs when the client is launched:

  https://docs.docker.com/engine/reference/builder/#entrypoint

The client container will then usually exit immediately.
