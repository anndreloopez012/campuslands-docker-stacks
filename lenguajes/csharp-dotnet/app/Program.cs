var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Campuslands C# stack funcionando");

app.Run();
