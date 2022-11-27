using Grpc.Core;
using Greeter;

namespace grpc_server.Services;

public class GreeterService : Greeter.Greeter.GreeterBase
{
    private readonly ILogger<GreeterService> _logger;
    public GreeterService(ILogger<GreeterService> logger)
    {
        _logger = logger;
    }

    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        _logger.LogDebug($"SayHello received: {request.Name}");
        return Task.FromResult(new HelloReply
        {
            Message = $"Hello, {request.Name}!" 
        });
    }

    public override async Task CounterStream(Empty request, IServerStreamWriter<CounterStreamReply> responseStream, ServerCallContext context)
    {
        int counter = 0;
        while (!context.CancellationToken.IsCancellationRequested)
        {
            _logger.LogDebug($"CounterStream generated: {counter}");
            await responseStream.WriteAsync(new CounterStreamReply {
                Counter = counter
            });
            counter += 1;
            await Task.Delay(TimeSpan.FromSeconds(1), context.CancellationToken);
        }
    }

    public override Task<NamesReply> GetNames(Empty request, ServerCallContext context)
    {
        _logger.LogDebug("GetNames called");
        return Task.FromResult(new NamesReply {
            Names = { "John", "Doe", "Mary" }
        });
    }
}
