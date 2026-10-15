
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	| 2.60 | 4.10 | 356.66 |
|   gRPC add	| 0.83 | 1.50 | 146.03 |
|   REST rawimg	| 6.48 | 10.91 | 1445.60 |
|   gRPC rawimg	| 13.83 | 15.44 | 468.82 |
|   REST dotproduct	| 3.18 | 4.48 | 381.34 |
|   gRPC dotproduct	| 0.93 | 1.61 | 309.74 |
|   REST jsonimg	| 24.41 | 28.66 | 1792.56 |
|   gRPC jsonimg	| 27.69 | 30.98 | 247.70 |
|   PING        | 0.05 | 0.68 | 159.16 |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

grpc was way faster for small stuff like add and dotproduct since it keeps one tcp connection open while rest makes a new one every request so rest pays the connection setup each time and that gets worse the more network latency there is. for the images they were kinda similar and rest was even a bit faster locally prob because sending the big payload dominates. but going to frankfurt grpc won by a lot on everything esp the images since the ping is like 160ms and rest has to redo the tcp handshake plus slow start every time
laptop:~/lab6-rest-vs-grpc$ 




